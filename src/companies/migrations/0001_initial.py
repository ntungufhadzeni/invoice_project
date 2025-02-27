# Generated by Django 5.0.4 on 2024-10-02 19:44

import companies.utils
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to=companies.utils.path_and_rename)),
                ('color', models.CharField(blank=True, max_length=25, null=True)),
                ('billing_address', models.TextField()),
                ('bank_name', models.CharField(max_length=30)),
                ('account_number', models.CharField(max_length=20)),
                ('branch_name', models.CharField(max_length=30)),
                ('branch_code', models.CharField(max_length=10)),
                ('branch_code_electronic', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('currency', models.CharField(choices=[('ZAR', 'South African Rand'), ('USD', 'US Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound')], default='ZAR', max_length=3)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
    ]
