# Generated by Django 5.0.1 on 2024-03-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_remove_feedbacktable_itemid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbacktable',
            name='userid',
        ),
        migrations.AddField(
            model_name='feedbacktable',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
