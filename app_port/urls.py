from django.urls import path
from app_port.views import enter, home

urlpatterns = [
    path('', enter, name='enter'),
    path('home/', home, name='home'),
]
