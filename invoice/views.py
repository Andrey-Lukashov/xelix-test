from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InvoiceForm
from .models import Invoice, Company
from .serializers import InvoiceSerializer


# Web views

def list_invoice(request):
    context = {}

    invoice_list = Invoice.objects.all().order_by('-date_posted')
    context['invoice_list'] = invoice_list

    return render(request, 'invoice_list.html', context=context)


def add_invoice(request):
    context = {}

    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        internal_reference = data.get('internal_reference')
        gross_amount = data.get('gross_amount')
        supplier_reference = data.get('supplier_reference')
        date_posted = data.get('date_posted')

        invoice = Invoice.objects.create(internal_reference=internal_reference,
                                         gross_amount=gross_amount,
                                         supplier_reference=supplier_reference,
                                         date_posted=date_posted,
                                         company=data.get('company'))

        invoice.save()
        context['message'] = 'Successfully added new invoice'
        form = InvoiceForm()
    else:
        context['message'] = 'Couldnt add invoice, form is invalid'
    context['form'] = form

    return render(request, 'invoice_create.html', context=context)


def search_invoice(request, internal_reference):
    context = {}

    invoiceS = Invoice.objects.filter(internal_reference=internal_reference)
    context['message'] = 'Searching for invoice with reference: ' + internal_reference
    context['invoice'] = invoiceS

    return render(request, 'search_invoice.html', context=context)


def search_company(request, company_id):
    context = {}

    company = get_object_or_404(Company,pk=company_id)
    context['message'] = 'Showing invoices for company: ' + company.name
    context['company'] = company
    return render(request, 'search_company.html', context=context)
