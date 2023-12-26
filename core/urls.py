from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('email/', views.email, name='email'),

    path('lodges/', views.lodges, name='lodges'),
    path('details/<lid>/', views.details, name='details'),
    path('caretaker/<pk>', views.caretaker, name='caretaker'),
    path("filter-products/", views.filter_product, name="filter-product"),





    
]