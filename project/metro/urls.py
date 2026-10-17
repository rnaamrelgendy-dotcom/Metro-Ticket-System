from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'station' , StationViewsets , basename= 'stationviewsets')
router.register(r'line' , LineViewsets , basename= 'lineviewsets')
router.register(r'ticket' , TicketList , basename= 'ticketlist')
router.register(r'user' , UserFilter , basename= 'userfilter')

urlpatterns = [
    path('' , include(router.urls)),
    path('ticketprice/' , TicketpriceCreate.as_view() , name= 'ticketpriceUpdate'),
    path('ticketprice/<int:pk>/' , TicketpriceUpdate.as_view() , name= 'ticketpriceUpdate'),
]