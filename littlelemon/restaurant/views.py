from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView , DestroyAPIView,ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import generics,viewsets
from rest_framework.response import Response


# Create your views here.



def index(request):
    return render(request, 'index.html' ,{})



@api_view()
@permission_classes([IsAuthenticated])
def message(request):
    return Response({"message: this view is protectes"})







class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  
    serializer_class = BookingSerializer



    