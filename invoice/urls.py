from django.contrib import admin
from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
    path('', views.list_invoice, name='list_invoice'),
    path('invoice/<str:internal_reference>/', views.search_invoice, name='search_invoice'),
    path('company/<int:company_id>/', views.search_company, name='search_company'),
    path('add/', views.add_invoice, name='add_invoice'),
]
