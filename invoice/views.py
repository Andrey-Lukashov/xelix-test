from django.views.generic import CreateView, TemplateView
from rest_framework import generics

from .forms import InvoiceForm
from .models import Invoice
from .serializers import InvoiceSerializer


# Web views

class ListInvoice(TemplateView):
    template_name = 'invoice_list.html'


class CreateInvoice(CreateView):
    template_name = 'invoice_create.html'
    model = Invoice
    form_class = InvoiceForm


# API (Django REST Framework) views

class APIInvoiceList(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
