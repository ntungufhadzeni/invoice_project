# Generated by Django 5.0.4 on 2025-07-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_invoice_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='template',
            field=models.CharField(blank=True, default='pdf_template.html', max_length=10),
        ),
    ]
