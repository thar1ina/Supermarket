# Generated by Django 4.2.9 on 2024-01-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_alter_prodyct_image_alter_prodyct_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('first_name', models.CharField(max_length=50)),
                ('availability', models.BooleanField(default=True, verbose_name='азыркы учурда иштейт')),
                ('image', models.ImageField(blank=True, upload_to='p/%Y/%m/%d')),
                ('position', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Описание')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт')),
            ],
        ),
    ]