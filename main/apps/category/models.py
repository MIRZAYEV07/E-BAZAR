from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ..common.models import BaseModel, BaseMeta


class Category(BaseModel):
    title = models.CharField(max_length=128)
    name = models.ForeignKey(
        'self',
        related_name='father',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    slug = models.CharField(max_length=128, unique=True)

    class Meta(BaseMeta):
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


    def __str__(self):

        if self.name:

            return self.name

        return self.title