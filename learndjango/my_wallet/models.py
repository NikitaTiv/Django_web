from django.db import models

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    time_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
