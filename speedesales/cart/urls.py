from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="cart"),
    path('add/', views.add_to_cart, name="add_to_cart"),
    path('remove/', views.remove_from_cart, name="rem_from_cart"),
    path('update/', views.update_cart, name="update_cart"),
]
