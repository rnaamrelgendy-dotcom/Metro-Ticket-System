from django.contrib import admin
from .models import *

admin.site.register(MetroLine)
admin.site.register(Station)
admin.site.register(TicketPrice)
admin.site.register(Ticket)