# Generated by Django 5.0.7 on 2024-08-01 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_vendor_vid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
        ),
    ]
