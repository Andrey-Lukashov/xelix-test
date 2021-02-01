from django import forms

from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['internal_reference', 'gross_amount', 'supplier_reference', 'date_posted']
