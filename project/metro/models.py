from django.db import models
from authentication.models import User


class MetroLine(models.Model):
    line_num = models.IntegerField()

    def __str__(self):
        return self.line_num

class Station(models.Model):
    name = models.CharField(max_length=100)
    line = models.ForeignKey(MetroLine , on_delete= models.CASCADE )
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class TicketPrice(models.Model):
    min_stations = models.IntegerField(null=True)
    max_stations = models.IntegerField(null= True)
    range_price = models.DecimalField(decimal_places=2 , max_digits=6)

    def __str__(self):
            return self.range
    
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="tickets_from")
    to_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="tickets_to")
    price = models.DecimalField( max_digits=6, decimal_places=2, null=True)

    def calculate_price(self):
        stations = abs( self.from_station.order - self.to_station.order )
        ticket_price = TicketPrice.objects.filter(
            min_stations__lte=stations,
            max_stations__gte=stations
        ).first()

        if ticket_price:
            return ticket_price.range_price

        return None

    def save(self, *args, **kwargs):
        self.price = self.calculate_price()
        super().save(*args, **kwargs)

    