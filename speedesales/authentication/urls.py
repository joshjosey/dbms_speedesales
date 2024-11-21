from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('register/',views.register_user, name="register"),
    path('update/',views.update_user, name="update"),
    
]
