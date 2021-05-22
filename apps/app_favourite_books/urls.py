from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard ),
    path('addbook', views.addbook ),
    path('<num>', views.detail ),
    path('delete/<num>', views.delete ),
    path('add_favourite/<num>', views.add_favourite ),
    path('delete_favourite/<num>', views.delete_favourite ),
    path('add_favourite_in_dash/<num>', views.add_favourite_in_dash ), 
    path('delete_favourite_in_dash/<num>', views.delete_favourite_in_dash ), 


]