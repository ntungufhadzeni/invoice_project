import uuid

from django.db import models


class Invoice(models.Model):
    TYPE_CHOICES = (
        ('INV', 'Invoice'),
        ('QUO', 'Quotation'),
    )

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=20)
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.TextField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    message = models.TextField(default="Thank you for doing business with us.")
    tax_rate = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0.00)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0.00)
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0.00)
    template = models.CharField(max_length=10, blank=True, default='pdf_template.html')
    status = models.BooleanField(default=False)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='INV')

    def __str__(self):
        return str(self.customer)

    def get_status(self):
        return self.status


class LineItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service_description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.invoice)
