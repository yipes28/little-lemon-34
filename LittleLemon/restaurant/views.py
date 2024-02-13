from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MenuItem, Booking
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, "index.html", {})


class MenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
