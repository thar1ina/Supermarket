# Generated by Django 4.2.9 on 2024-01-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_prodyct_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodyct',
            name='image',
            field=models.ImageField(blank=True, upload_to='p/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='prodyct',
            name='weight',
            field=models.CharField(max_length=50, verbose_name='Вес'),
        ),
    ]