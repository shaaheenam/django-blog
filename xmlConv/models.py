from django.db import models
from django.urls import reverse

# static database model

class Files(models.Model):
    xmlfile = models.FileField(upload_to='files/')

    def get_absolute_url(self):
        return reverse('xmltopdf')

class Customers(models.Model):

    customerID = models.CharField(max_length=200, blank=True)
    companyName = models.CharField(max_length=200, blank=True)
    contactName = models.CharField(max_length=200, blank=True)
    contactTitle = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    fax = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    region = models.CharField(max_length=200, blank=True)
    postalCode = models.IntegerField()
    country = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.contactName


class Orders(models.Model):

    customerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    employeeID = models.IntegerField()
    orderDate = models.DateTimeField()
    requiredDate = models.DateTimeField()
    shippedDate = models.DateTimeField(null=True)
    shipVia = models.IntegerField()
    freight = models.FloatField()
    shipName = models.CharField(max_length=200, blank=True)
    shipAddress = models.CharField(max_length=200, blank=True)
    shipCity = models.CharField(max_length=200, blank=True)
    shipRegion = models.CharField(max_length=200, blank=True)
    shipPostalCode = models.IntegerField()
    shipCountry = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.shipName


# need to create a dynamic model later