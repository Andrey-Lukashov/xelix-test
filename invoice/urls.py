from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create', views.CreateInvoice.as_view()),
    path('', views.ListInvoice.as_view()),
    path('api/invoice/', views.APIInvoiceList.as_view())
]
