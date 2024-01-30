from django.urls import path

from . import views

app_name = 'userauths'

urlpatterns = [
    path('register/', views.reg, name='register'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),


    
]