from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'kvyat'
urlpatterns = [
    path('', views.create, name='create'),
    path('room/', views.room, name='room'),
    path('login/', auth_views.LoginView.as_view(template_name='kvyat/login.html'), name="login"),
    path('register/', views.register_view, name='register'),
    path('<int:user_id>/profile', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('creator/', views.creator, name='creator'),
    path('contact/', views.contact, name='contact'),
    path('login_user/', views.login_user, name='login_user'),
    path('<int:user_id>/logout_user/', views.logout_user, name='logout_user'),
    path('upload_points/<int:user_id>/<int:guesses>', views.upload_points, name='upload_points')
]