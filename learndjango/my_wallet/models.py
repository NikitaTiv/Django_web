from django.db import models
from django.urls import reverse


class Wallet(models.Model):
    name = models.CharField(max_length=50)
    time_update = models.DateField(auto_now=True)
    time_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wallet_info', kwargs={'wallet_id': self.pk})


class Transaction(models.Model):
    description = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    time_create = models.DateTimeField(auto_now_add=True)
    wallet = models.ForeignKey('Wallet', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.description


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'
        ordering = ['time_create', 'id']
