# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("pay/", views.payment_view, name="payment_view"),
]
