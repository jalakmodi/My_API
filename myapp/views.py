from django.shortcuts import render
from rest_framework import generics
from .models import Msg
from .serializers import MsgSerializer

# Create your views here.

class MsgList(generics.ListCreateAPIView):
	queryset=Msg.objects.all()
	serializer_class=MsgSerializer

class MsgDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Msg
	serializer_class=MsgSerializer