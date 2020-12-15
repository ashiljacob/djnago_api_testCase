from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    gstin = models.CharField(max_length=50)
    outstandingbalance = models.FloatField()

    def __str__(self):
        return self.name
    