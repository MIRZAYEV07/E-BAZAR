import os

from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from django.db import models

from main.apps.common.models import BaseModel


def upload_profile_images(instance, filename):
    filename_without_extension, extension = os.path.splitext(filename.lower())
    timestamp = timezone.now().strftime("%Y-%m-%d.%H-%M-%S")
    filename = f"{slugify(filename_without_extension)}.{timestamp}{extension}"
    return f"product/{filename}"

class ProductImage(BaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to=upload_profile_images)
    is_main = models.BooleanField(default=False)




    class Meta:
        ordering = ("id",)
        verbose_name = _("ProductImage")
        verbose_name_plural = _("ProductImagess")

    def __str__(self) -> str:
        return self.title

