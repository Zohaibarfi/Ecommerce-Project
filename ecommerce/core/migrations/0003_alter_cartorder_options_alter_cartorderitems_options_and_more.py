# Generated by Django 5.0.7 on 2024-07-27 06:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_oder_date_cartorder_order_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name_plural': 'Cart Order'},
        ),
        migrations.AlterModelOptions(
            name='cartorderitems',
            options={'verbose_name_plural': 'Cart Order Items'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='categroy',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='specificatios',
            new_name='specifications',
        ),
        migrations.AlterField(
            model_name='category',
            name='cid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
