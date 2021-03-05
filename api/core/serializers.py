from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username

        return token

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'symbol', 'description', 'sector',
                  'market_cap', 'country', 'index']

class StockExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockExchange
        fields = ['name', 'mic', 'market_place', 'region',
                  'market_cap']
