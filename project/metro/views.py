from django.shortcuts import render
from .models import *
from authentication.models import User
from .serializers import * 
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from authentication.permissions import IsOwner,IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class StationViewsets(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [IsAdmin]

class TicketpriceCreate(ListCreateAPIView):
    queryset = TicketPrice.objects.all()
    serializer_class = TicketPriceSerializer
    permission_classes = [IsAdmin]

class TicketpriceUpdate(RetrieveUpdateDestroyAPIView):
    queryset = TicketPrice.objects.all()
    serializer_class = TicketPriceSerializer
    permission_classes = [IsAdmin]

class LineViewsets(viewsets.ModelViewSet):
    queryset = MetroLine.objects.all()
    serializer_class = MetroLineSerilizer
    permission_classes = [IsAdmin]

class TicketList(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated and (IsOwner or IsAdmin)]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'manager':
            return Ticket.objects.all()
        else:
            return Ticket.objects.filter(user = user)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter , filters.OrderingFilter]
    filterset_fields = ['price' , 'user']
    search_fields = ['user' , 'from_station' , 'to_station']
    ordering_fileds = ['price']

class UserFilter(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    filter_backends = [DjangoFilterBackend , filters.SearchFilter]
    filterset_fields = ['username']
    search_fields = ['username']