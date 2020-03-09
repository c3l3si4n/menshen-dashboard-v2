from django.conf.urls import url
from .views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    url("signup", signup, name='signup'),
    url("password_reset_done", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url("password_reset_confirm", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url("password_reset_complete", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url("password_reset", auth_views.PasswordResetView.as_view(), name='password_reset'),
    url('login', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),
    url('logout', auth_views.LogoutView.as_view(next_page='/'), name='login'),

]