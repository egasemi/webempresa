from django.urls import include, path
from .views import *

urlpatterns = [

    path('', services, name="services"),

]