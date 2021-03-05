from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .serializers import *
from rest_framework import status
from .models import Company, StockExchange
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import Http404
from rest_framework import generics, mixins



class MyObtainTokenPairView(TokenObtainPairView):

    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CompanyList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        market = Company.objects.all()
        serializer = CompanySerializer(market, many=True)
        return Response(serializer.data)

class CompanyDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, symbol):

        try:
            return Company.objects.get(symbol=symbol.upper())
        except:
            raise Http404

    def get(self, request, symbol):
        company = self.get_object(symbol)
        serializer = CompanySerializer(company)
        return Response(serializer.data)


class CompanyAdd(APIView):
    permission_classes = (IsAdminUser,)
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyAdmin(APIView):
    permission_classes = (IsAdminUser,)

    def get_object(self, symbol):
        try:
            company = Company.objects.get(symbol=symbol.upper())
            return company
        except:
            raise Http404

    def get(self, request, symbol):
        company = self.get_object(symbol)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, symbol):
        company = self.get_object(symbol)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, symbol):
        company = self.get_object(symbol)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MarketList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        market = StockExchange.objects.all()
        serializer = StockExchangeSerializer(market, many=True)
        return Response(serializer.data)

class MarketDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, mic):

        try:
            return StockExchange.objects.get(mic=mic.upper())
        except:
            raise Http404

    def get(self, request, mic):
        market = self.get_object(mic)
        serializer = StockExchangeSerializer(market)
        return Response(serializer.data)


class MarketAdmin(APIView):
    permission_classes = (IsAdminUser,)

    def get_object(self, mic):

        try:
            return StockExchange.objects.get(mic=mic.upper())
        except:
            raise Http404

    def get(self, request, mic):
        market = self.get_object(mic)
        serializer = StockExchangeSerializer(market)
        return Response(serializer.data)

    def put(self, request, mic):
        market = self.get_object(mic)

        serializer = StockExchangeSerializer(market, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mic):
        market = self.get_object(mic)
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MarketAdd(APIView):
    permission_classes = (IsAdminUser,)
    def post(self, request, format=None):
        serializer = StockExchangeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
