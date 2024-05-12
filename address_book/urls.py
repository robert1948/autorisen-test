from django.urls import path
from . import views

urlpatterns = [
path("add_address", views.add_address, name="add_address"),    
]
