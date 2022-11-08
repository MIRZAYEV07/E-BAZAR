from django.db import models
from main.apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _



class MainFeatureType(BaseModel):

    title = models.CharField(max_length=128)



    class Meta:
        ordering = ("id",)
        verbose_name = _("MainFeatureType")
        verbose_name_plural = _("MainFeatureTypes")

    def __str__(self) -> str:
        return self.title

class MainFeatureValue(BaseModel):

    title = models.CharField(max_length=128)
    type = models.ForeignKey(
            MainFeatureType,
            on_delete=models.CASCADE,
            related_name='values'
    )



    class Meta:
        ordering = ("id",)
        verbose_name = _("MainFeatureValue")
        verbose_name_plural = _("MainFeatureValues")

    def __str__(self) -> str:
        return self.title


