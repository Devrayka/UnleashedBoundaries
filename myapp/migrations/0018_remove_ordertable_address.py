# Generated by Django 5.0.1 on 2024-03-16 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_ordertable_date_remove_ordertable_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordertable',
            name='address',
        ),
    ]
