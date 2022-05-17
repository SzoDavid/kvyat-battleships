from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'kvyat'
urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
    path('login/', auth_views.LoginView.as_view(template_name='kvyat/login.html', next_page='/kvyat/',
                                                redirect_authenticated_user=True), name="login"),
    path('register/', views.register_view, name='register'),
    path('<int:user_id>/profile', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('upload_points/<int:user_id>/<int:guesses>', views.upload_points, name='upload_points')
]