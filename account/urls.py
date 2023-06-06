from django.contrib.auth import views as auth_views
from django.urls import path
from . import views



app_name='account'

urlpatterns = [
    path('login_user/',views.login_user, name='login_user'),
    path('logged_in/', views.loged_in, name='loged_in'),
    path('', views.logged_out, name='logged_out'),
    # promena lozinke
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    # zaboravili ste vasu lozinku
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/',views.edit, name='edit'),

]