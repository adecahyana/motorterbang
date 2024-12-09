# Generated by Django 5.1.3 on 2024-11-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=200)),
                ('no_katalog', models.CharField(max_length=50)),
                ('spesifikasi', models.TextField()),
                ('stok', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pdn', models.BooleanField(default=True)),
            ],
        ),
    ]
