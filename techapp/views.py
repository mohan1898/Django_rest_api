from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mobile
from .serializer import MobileSerializer

@api_view(['GET'])
def mobileinfo(request):
    mob=Mobile.objects.all()
    serializer=MobileSerializer(mob,many=True)
    return Response(serializer.data)


