# Generated by Django 5.1.3 on 2024-11-18 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_order_customer_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='General', on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
