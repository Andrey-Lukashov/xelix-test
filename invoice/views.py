from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InvoiceForm
from .models import Invoice
from .serializers import InvoiceSerializer


# Web views

def list_invoice(request):
    context = {}

    invoice_list = Invoice.objects.all().order_by('-date_posted')
    context['invoice_list'] = invoice_list

    return render(request, 'invoice_list.html', context=context)


def add_invoice(request):
    context = {}

    form = InvoiceForm()
    context['form'] = form

    return render(request, 'add_invoice.html', context=context)