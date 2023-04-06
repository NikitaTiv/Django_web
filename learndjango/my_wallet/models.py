from django.db import models


class Wallet(models.Model):
    name = models.CharField(max_length=50)
    time_update = models.DateTimeField(auto_now=True)
    time_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    desctiprion = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
