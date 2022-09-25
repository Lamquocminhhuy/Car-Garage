from dataclasses import field
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Booking, Service

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'price', 'time_todo', 'description', 'image']

class BookingSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Booking
        fields = '__all__' 