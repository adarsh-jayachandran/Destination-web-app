from django.urls import path 
from . import views

urlpatterns = [
    path('register',views.register,name = 'register'),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("destination/<int:id>/",views.destination_detail,name='destination_detail')
]