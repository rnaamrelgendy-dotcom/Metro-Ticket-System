from rest_framework import serializers
from .models import * 
from authentication.models import User

class MetroLineSerilizer(serializers.ModelSerializer):
    class Meta:
        model = MetroLine
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class TicketPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPrice
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"