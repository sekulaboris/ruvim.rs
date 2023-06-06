from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name='Contact'

urlpatterns = [
    path('contact/',views.contact_view, name='contact'),
    
] 