from django.urls import include, path
from .views import *

urlpatterns = [

    path('', home, name="home"),
    path('about/', about, name='about'),
    path('store/', store, name='store'),
]