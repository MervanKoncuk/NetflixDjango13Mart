# Generated by Django 4.2 on 2023-05-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_hesap_sifre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hesap',
            name='resim',
            field=models.ImageField(blank=True, upload_to='hesaplar/'),
        ),
    ]