from django.db import models

class Prodyct(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    weight = models.CharField(max_length=50, verbose_name='Вес')
    price = models.FloatField(verbose_name='Цена')
    term = models.DateTimeField(verbose_name='Срок изготовления')
    image = models.ImageField(upload_to='p/%Y/%m/%d', blank=True)
    compoud = models.TextField(max_length=400, verbose_name='Состав' )



    def __str__(self):
        return f'{self.name} - {self.image}'


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    first_name = models.CharField(max_length=50)

    availability = models.BooleanField(default=True, verbose_name='азыркы учурда иштейт')
    image = models.ImageField(upload_to='p/%Y/%m/%d', blank=True)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(max_length=1000, blank=True,verbose_name='Описание')
    website = models.URLField(max_length=200, blank=True, null=True,verbose_name='Ссылка на сайт')

    def __str__(self):
        return f'{self.name} - {self.image}'