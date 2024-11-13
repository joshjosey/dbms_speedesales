from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('technology/', views.tech, name='tech'),
    path('category/<str:category>', views.product_category, name='category'),
]
