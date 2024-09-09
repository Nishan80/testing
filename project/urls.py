from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Connect the home view to the root URL
]
