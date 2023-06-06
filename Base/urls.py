from django.urls import path
from . import views


app_name='Base'

urlpatterns = [
    path('', views.onama, name='onama'),
    path('onama/',views.onama, name='onama'),
    path('search/',views.search, name='search'),
    
]