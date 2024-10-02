import re

from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Invoice, LineItem


class InvoiceForm(forms.Form):

    def clean_due_date(self):
        """
        Custom clean method to ensure that the due date is greater than today.
        """
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date <= timezone.now().date():
            raise ValidationError('Due date must be greater than today.')
        return due_date

    def clean_tax_rate(self):
        """
        Custom clean method to ensure that the tax rate is not negative.
        """
        try:
            rate = float(self.cleaned_data.get('tax_rate', 0))
            if rate < 0:
                raise ValidationError('Tax rate cannot be negative.')
        except Exception as e:
            raise ValidationError('Tax rate can only be a number.')

        return rate

    def clean_customer_email(self):
        """
        Custom clean method to ensure that the customer email is valid.
        """
        # Regular expression for a basic email validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email = self.cleaned_data.get('customer_email', '')
        if not email:
            return email
        # Using re.match() to check if the email matches the pattern
        if not re.match(email_regex, email):
            raise ValidationError('Enter a valid email address or leave it blank.')
        return email

    def clean_customer_phone(self):
        # Regular expression for a South African phone validation
        phone_regex = r'^0[1-9]\d{8}$'
        phone = self.cleaned_data.get('customer_phone', '')
        if not phone:
            return phone
        # Using re.match() to check if the phone matches the pattern
        if not re.match(phone_regex, phone):
            raise ValidationError('Invalid phone number format..')
        return phone

    class Meta:
        model = Invoice

    invoice_number = forms.CharField(
        label='#',
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Invoice/Quotation Number',
            'hx-post': reverse_lazy('invoice_number_validation'),
            'hx-target': '#invoiceNumberError',
            'hx-swap': 'outerHTML',
            'hx-select': '#invoiceNumberError',
            'hx-select-oob': '#saveBtn',
            'hx-trigger': 'keyup[target.value.length > 0]'
        }),
    )
    customer = forms.CharField(
        label='Customer Name',
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Customer/Company Name',
            'rows': 1
        })
    )
    customer_email = forms.CharField(
        label='Customer Email',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'customer@company.com',
            'rows': 1
        })
    )
    billing_address = forms.CharField(
        label='Customer Address',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'input',
            'placeholder': '1234 Bobcat Lane St.\nProtea\n1818',
            'rows': 4
        })
    )
    message = forms.CharField(
        label='Message/Note',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'input',
            'placeholder': 'Message/Note to customer',
            'rows': 3
        })
    )
    tax_rate = forms.DecimalField(
        label='Tax (%)',
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Value added tax (VAT) e.g. 15',
                'rows': 1
            })
    )
    type = forms.ChoiceField(choices=Invoice.TYPE_CHOICES)
    date = forms.DateField(
        label='Date',
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd',
                'class': 'input'})
    )
    due_date = forms.DateField(
        label='Due-Date',
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'yyyy-mm-dd',
                'class': 'input'})
    )
    customer_phone = forms.CharField(
        label='Customer Phone',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': '0862223333',
            'rows': 1
        }),
    )


class LineItemForm(forms.Form):
    class Meta:
        model = LineItem

    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Enter product/service description',
            'rows': 1
        })
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity e.g. 32'
        })  # quantity should not be less than one
    )
    rate = forms.DecimalField(
        label='Unit Price',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Unit Price e.g. 299.99'
        })
    )


LineItemFormSet = formset_factory(LineItemForm, extra=1)
