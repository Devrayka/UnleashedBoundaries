# Generated by Django 5.0.1 on 2024-01-30 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admintable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('phonenumber', models.BigIntegerField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='areatable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='categorytable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='usertable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
                ('password', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='itemtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='photos')),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=10)),
                ('price', models.FloatField()),
                ('discription', models.TextField()),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categorytable')),
            ],
        ),
        migrations.CreateModel(
            name='carttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.BigIntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=10)),
                ('amount', models.FloatField()),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.itemtable')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='ordertable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('address', models.TextField()),
                ('paymentmode', models.CharField(max_length=20)),
                ('totalbill', models.FloatField()),
                ('cartid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.carttable')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='pitchtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('areaid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.areatable')),
            ],
        ),
        migrations.CreateModel(
            name='paymenttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentmode', models.CharField(max_length=20)),
                ('location', models.TextField()),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.itemtable')),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ordertable')),
                ('pitchid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pitchtable')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='feedbacktable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('comment', models.TextField()),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.itemtable')),
                ('pitchid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pitchtable')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='complaintable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.itemtable')),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ordertable')),
                ('pitchid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pitchtable')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='bookingtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingdate', models.DateField()),
                ('bookingtime', models.TimeField()),
                ('paymentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.paymenttable')),
                ('pitchid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pitchtable')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usertable')),
            ],
        ),
    ]
