# Generated by Django 5.0.1 on 2024-03-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_bookingtable_pitchid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordertable',
            name='cartid',
        ),
        migrations.RemoveField(
            model_name='ordertable',
            name='status',
        ),
        migrations.AddField(
            model_name='ordertable',
            name='orderstatus',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='ordertable',
            name='phonenumber',
            field=models.BigIntegerField(null=True),
        ),
    ]
