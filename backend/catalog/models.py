from django.db import models

from users.models import User


class Region(models.Model):
    """ Регион."""
    name = models.CharField(
        'Название региона',
        max_length=150
    )

    def __str__(self):
        return self.name


class Supplier(models.Model):
    """ Поставщики."""
    name = models.CharField(
        'Название поставщика',
        max_length=200,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='supplier_profile'
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='suppliers',
        verbose_name='Регион'
    )

    def __str__(self):
        return f'{self.name} ({self.region})'


class Buyer(models.Model):
    """ Покупатели. """
    name = models.CharField(
        'Название организации',
        max_length=150
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='buyer'
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='organizations',
        verbose_name='Регион'
    )

    def __str__(self):
        return f'{self.name} ({self.region})'


class Product(models.Model):
    """ Продукт."""
    name = models.CharField(
        'Название продукта',
        max_length=200
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Поставщик'
    )
    quantity = models.PositiveIntegerField('Колличество')

    def __str__(self):
        return f'{self.name} ({self.quantity}) от {self.supplier}'


class Request(models.Model):
    """ """
    product_name = models.CharField(
        'Название продукта',
        max_length=200
    )
    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
        related_name='requests',
        verbose_name='Покупатель'
    )
    quantity = models.PositiveIntegerField('Колличество')

    def __str__(self):
        return f'{self.product_name} ({self.quantity}) для {self.buyer}'
