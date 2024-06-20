from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('', views.index, name='index'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='membership/password_reset.html'), name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='membership/password_reset_sent.html'), name="password_reset_sent"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='membership/password_reset_form.html'), name="password_reset_confirm"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='membership/password_reset_form.html'), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='membership/password_reset_done.html'), name="password_reset_complete"),
    path('update_password/', views.update_password, name='update_password'),
    path('update_email/', views.update_email, name='update_email'),
]