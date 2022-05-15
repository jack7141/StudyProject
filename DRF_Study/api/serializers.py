from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Reviews

class ProductFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ['username']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']