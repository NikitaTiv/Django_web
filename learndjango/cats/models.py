from django.db import models


class Cats(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_posted = models.DateField()
    time_upload = models.DateField(auto_now_add=True)
