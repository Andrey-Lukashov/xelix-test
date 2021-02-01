from django.contrib import admin
from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
    path('', views.list_invoice, name='list_invoice'),
    path('add/', views.add_invoice, name='add_invoice'),
    path('invoices_per_company/<int:company_id>', views.invoice_detail, name='invoice_detail'),
]
