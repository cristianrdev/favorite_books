from django.urls import path
from . import views
from apps.app_login_register import views

urlpatterns = [
    path('', views.index ),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout ),

]