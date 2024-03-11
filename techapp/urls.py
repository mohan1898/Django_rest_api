
from django.urls import path
from techapp import views

urlpatterns = [
    path('',views.mobileinfo,name='mobileinfo'),
]
