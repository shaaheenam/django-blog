# Generated by Django 4.1.4 on 2023-02-02 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(blank=True, max_length=200)),
                ('companyName', models.CharField(blank=True, max_length=200)),
                ('contactName', models.CharField(blank=True, max_length=200)),
                ('contactTitle', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('fax', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('region', models.CharField(blank=True, max_length=200)),
                ('postalCode', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xmlfile', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeID', models.IntegerField()),
                ('orderDate', models.DateTimeField()),
                ('requiredDate', models.DateTimeField()),
                ('shippedDate', models.DateTimeField(null=True)),
                ('shipVia', models.IntegerField()),
                ('freight', models.FloatField()),
                ('shipName', models.CharField(blank=True, max_length=200)),
                ('shipAddress', models.CharField(blank=True, max_length=200)),
                ('shipCity', models.CharField(blank=True, max_length=200)),
                ('shipRegion', models.CharField(blank=True, max_length=200)),
                ('shipPostalCode', models.IntegerField()),
                ('shipCountry', models.CharField(blank=True, max_length=200)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmlConv.customers')),
            ],
        ),
    ]