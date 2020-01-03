from django.urls import path
from . import views


urlpatterns = [

    path('home',views.home),
    path('Register',views.Register),
    path('reg',views.reg),
    path('login',views.login),
    path('logo',views.logo)
]