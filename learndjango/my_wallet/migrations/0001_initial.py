# Generated by Django 4.1.7 on 2023-05-26 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateField(auto_now_add=True, verbose_name='Время создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['time_create', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.CharField(max_length=30)),
                ('time_update', models.DateField(auto_now=True)),
                ('time_create', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_wallet.wallet')),
            ],
        ),
    ]
