# Generated by Django 5.1 on 2024-08-27 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, unique=True)),
                ('work_time', models.CharField(choices=[('10:00-20:00', '10:00-20:00'), ('09:00-19:00', '09:00-19:00'), ('08:00-18:00', '08:00-18:00')], max_length=100)),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('count_sell', models.IntegerField()),
                ('avatar', models.ImageField(upload_to='store_avatars/')),
                ('banner', models.ImageField(upload_to='store_banners/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count', models.IntegerField(default=0)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='products_images/')),
                ('aksiya', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olma_app.category')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olma_app.store')),
            ],
        ),
    ]
