from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:category>', views.product_category, name='category'),
    path('view_orders/', views.view_orders, name='view_orders'),
]
