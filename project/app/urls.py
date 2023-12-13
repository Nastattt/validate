from django.urls import path
from .views import *

urlpatterns = [
    path('my',index,name = 'home'),
    path('data',getData,name= 'data')
]