from django.urls import path
from django.contrib.auth import views
from usersapp.views import register_view

urlpatterns = [
    path ('register/', register_view, name='register'),
    path ('login/', views.LoginView.as_view(template_name='usersapp/login.html'), name='login'),
    path ('logout/', views.LogoutView.as_view(template_name='usersapp/logout.html'), name='logout'),
    path ('change-password/', views.PasswordChangeView.as_view(template_name='usersapp/changepassword.html'), name='password_change'),
    path ('password-change-done/', views.PasswordChangeDoneView.as_view(template_name='usersapp/passwordsuccess.html'), name='password_change_done')
]