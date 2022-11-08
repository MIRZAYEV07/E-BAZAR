from django.db import models
from django.utils.translation import gettext_lazy as _

from main.apps.common.models import BaseModel
from main.apps.account.models.user import User

from ..models.product import ProductModel

class Comments(BaseModel):

    class RatingsChoice(models.TextChoices):
        FIVE = '5'
        FOUR = '4'
        THREE = '3'
        TWO = '2'
        ONE = '1'

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(
            ProductModel,
            on_delete=models.CASCADE,
            related_name='comments'
        )
    text = models.TextField()

    author_name = models.CharField(max_length=128)
    rating = models.CharField(
            max_length=128,
            choices=RatingsChoice.choices,
            default=RatingsChoice.FIVE
        )


    

    class Meta:
        ordering = ("id",)
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self) -> str:
        return self.author_name
