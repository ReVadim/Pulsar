from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator

from src.base.services import (
    WEBPField,
    get_path_upload_image,
    validate_size_image,
)


class Products(models.Model):
    """ Main product model """
    STATUS = (
        ('AVAILABLE', 'В наличии'),
        ('UNAVAILABLE', 'Нет в наличии'),
        ('EXPECTED', 'Ожидается поступление'),
        ('NOT_PRODUCED', 'Не производится'),
        ('BY_ORDER', 'Под заказ'),
    )

    title = models.CharField(max_length=100, verbose_name=_("title"))
    article = models.CharField(max_length=30, verbose_name=_("article"))
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField(choices=STATUS, max_length=22, verbose_name=_("status"), default='AVAILABLE')
    image = WEBPField(
        upload_to=get_path_upload_image,
        blank=True,
        null=True,
        verbose_name=_("image"),
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'webp']), validate_size_image]
    )

    def __str__(self):
        return f'{self.article} - {self.title}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('status',)
