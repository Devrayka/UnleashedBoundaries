# Generated by Django 5.0.1 on 2024-03-11 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_carttable_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingtable',
            name='pitchid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.pitchtable'),
        ),
    ]
