from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.AccountCreateView.as_view())  
]

