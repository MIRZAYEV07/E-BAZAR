from django.db import models
from main.apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _


class SubFeatureType(BaseModel):
    title = models.CharField(max_length=128)



    class Meta:
        ordering = ("id",)
        verbose_name = _("SubFeatureType")
        verbose_name_plural = _("SubFeatureTypes")

    def __str__(self) -> str:
        return self.title


class SubFeatureValue(BaseModel):
    title = models.CharField(max_length=128)
    type = models.ForeignKey(
        SubFeatureType,
        on_delete=models.CASCADE,
        related_name='values'
    )



    class Meta:
        ordering = ("id",)
        verbose_name = _("SubFeatureValue")
        verbose_name_plural = _("SubFeatureValues")

    def __str__(self) -> str:
        return self.title
