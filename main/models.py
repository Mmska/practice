from django.db import models


class Product(models.Model):
    title = models.CharField(
        max_length=255, blank=False, verbose_name="Название"
    )
    image = models.ImageField(upload_to='products', null=True, blank=True)
    description = models.TextField(verbose_name="Описание", default='', blank=True)
    # цена за штуку в рублях
    price = models.DecimalField(
        max_digits=12, decimal_places=2, verbose_name="Цена"
    )
    oroginal_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="Цена без скидкой")
    count = models.IntegerField(default=0, verbose_name="Количество")
    is_active = models.BooleanField(default=True, verbose_name='Активен?')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title
