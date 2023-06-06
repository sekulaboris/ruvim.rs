from django.urls import path
from . import views

app_name='payment'

urlpatterns=[
    path('process/',views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
    #path('<int:order_id>/stampajII_pdf/', views.stampajII_pdf, name='stampajII_pdf'),
    
]