import os

from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from django.db import models
from main.apps.common.models import BaseModel
from main.apps.account.models.user import User


def upload_profile_images(instance, filename):
    filename_without_extension, extension = os.path.splitext(filename.lower())
    timestamp = timezone.now().strftime("%Y-%m-%d.%H-%M-%S")
    filename = f"{slugify(filename_without_extension)}.{timestamp}{extension}"
    return f"product/{filename}"

class CartModel(BaseModel):

    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=128, unique=True)

    cart_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart_owner'

    )

    pictures = models.ImageField(upload_to=upload_profile_images)
    brand_tag = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    price_for_credit = models.IntegerField(default=0)
    product_number = models.IntegerField(default=1)

    class Meta:
        ordering = ("id",)
        verbose_name = _("CartModel")
        verbose_name_plural = _("CartModel")

    def __str__(self) -> str:
        return self.title

class TotalCartModel(BaseModel):

    title = models.CharField(max_length=256)

    cart = models.ForeignKey(
        CartModel,
        on_delete=models.CASCADE,
        related_name='cart'

    )

    product_number_in_cart = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

    class Meta:
        ordering = ("id",)
        verbose_name = _("TotalCartModel")
        verbose_name_plural = _("TotalCartModel")

    def __str__(self) -> str:
        return self.title



