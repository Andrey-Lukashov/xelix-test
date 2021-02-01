from django import forms

from .models import Invoice


class DateInput(forms.DateInput):
    input_type = 'date'


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['internal_reference', 'gross_amount', 'supplier_reference', 'date_posted', 'company_name']
        widgets = {
            'date_posted': DateInput()
        }