from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('lodges/', views.lodge, name='lodges'),
    path('contact/', views.Contact, name='contact'),
    path("delete-products/<lid>/", views.delete_product, name="delete-products"),
    path("dashboard-edit/<lid>/", views.dashboard_edit, name="dashboard-edit"),
    path("profile/", views.profile, name='profile'),
    path("edit-profile/", views.edit_profile, name='edit-profile'),







    
]