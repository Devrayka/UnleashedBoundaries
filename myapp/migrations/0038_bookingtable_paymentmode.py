# Generated by Django 5.0.1 on 2024-03-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_bookingtable_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtable',
            name='paymentmode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
