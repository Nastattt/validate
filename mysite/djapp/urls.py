from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('', sign_in),
    path('successful/', successful),
    path('reg/', reg, name="reg"),
    path('reg/congrats/', congrats, name="congrats"),
    path('forget/', forget),
]


