from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, profile_view, home_view, search_view, connect_request_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('search/', search_view, name='search'),
    path('connect/<int:user_id>/', connect_request_view, name='connect'),
]
