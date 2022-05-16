from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('' ,  views.home  , name="home"),
    path('register/' , views.register_attempt , name="register_attempt"),
    path('login/' , views.login_attempt , name="login_attempt"),
    path('logout' , views.logout , name="logout"),
    path('token/' , views.token_send , name="token_send"),
    path('success/' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error/' , views.error_page , name="error"),
    path('password_reset', views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),      

    
   
]