from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LoginUsersView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
