from django.shortcuts import render
from rest_framework import generics
from .models import Account
from .serializers import AccountSeralizer

class AccountCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSeralizer