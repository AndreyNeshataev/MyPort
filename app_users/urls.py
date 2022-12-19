from django.urls import path
from app_users.views import LoginUser

urlpatterns = [
    # path('register/', RegisterUser.as_view(), name='register_url'),
    path('login/', LoginUser.as_view(), name='login_url'),
]
