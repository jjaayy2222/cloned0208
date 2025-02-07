from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path(
        "login/",# `auth_views.LoginView.as_view(template_name="accounts/login.html")` is creating a
        # view for the login functionality in Django. The `template_name` parameter specifies
        # the template file to be used for rendering the login page.
        
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="home/"), name="logout"), # 로그아웃 후 "home/"으로 이동 
    path('profile/update/', views.profile_update, name='profile_update')
]
