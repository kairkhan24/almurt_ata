from django.db import models

from src.common.models import BaseModel

class Restaurant(BaseModel):
    """A restaurant that prepares pizza."""

    name = models.CharField(max_length=128, verbose_name='Название')
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name='Адрес')

    def __str__(self):
        return f'{self.id} | {self.name}'

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'


class Pizza(BaseModel):
    "A pizza with own recipe."

    name = models.CharField(max_length=128, verbose_name="Название")
    cheese = models.CharField(max_length=128, blank=True, null=True, verbose_name="Вид cыра")
    pastry = models.CharField(max_length=128, blank=True, null=True, verbose_name="Толщина теста")
    secret_ingredient = models.CharField(max_length=128, blank=True, null=True, verbose_name="Секретный ингредиент")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='pizzas', verbose_name='Ресторан')

    def __str__(self):
        return f'{self.id} | {self.name}'

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
