from rest_framework import serializers
from .models import *


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['firstName', 'lastName', 'street', 'city', 'state', 'zip']


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['firstName', 'lastName']