from django.urls import include, path
from .views import *

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>', page, name='page')
]