from typing import Optional
from django.db import models
from csfe_django.utilities import Validators


# Create your models here.


class Status(models.Model):
    title = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    root = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


class Table(models.Model):
    capacity = models.IntegerField(
        null=False,
        blank=False
    )
    position_space = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )
    status = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        default=12,
        null=True,
        blank=True
    )


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
        unique=True
    )
    root = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )


class MenuItems(models.Model):
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    price = models.IntegerField(
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    discount = models.IntegerField(
        default=0,
    )
    image_name = models.CharField(
        max_length=100
    )
    cooking_time = models.TimeField(
        null=True,
        blank=True
    )
    serving_time = models.TimeField(
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        to=Status,
        on_delete=models.CASCADE
    )


class Recepites(models.Model):
    total_price = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    final_price = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    status = models.ForeignKey(
        to=Status,
        on_delete=models.CASCADE

    )
    table_number = models.ForeignKey(
        to=Table,
        on_delete=models.CASCADE
    )


class Orders(models.Model):
    count = models.IntegerField(
        default=0,
    )
    time_stamp = models.TimeField(
        null=False
    )
    status = models.ForeignKey(
        to=Status,
        on_delete=models.CASCADE
    )
    recepite = models.ForeignKey(
        to=Recepites,
        on_delete=models.CASCADE
    )
    menu_item = models.ForeignKey(
        to=MenuItems,
        on_delete=models.CASCADE
    )


class Massages(models.Model):
    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=9,
        validators=[Validators.check_phone],
        null=False,
        blank=False
    )
    email = models.fields.EmailField(
        max_length=100,
        null=True,
        blank=True
    )
    comment = models.TextField(
        null=False
    )
