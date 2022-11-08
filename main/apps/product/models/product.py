from django.db.models import Avg
from django.utils.translation import gettext_lazy as _

from django.db import models
from main.apps.common.models import BaseModel
from main.apps.category.models import Category
from main.apps.account.models.user import User

from .main_features import MainFeatureType
from .sub_features import SubFeatureType
from .images import ProductImage
from ..managers.product import ProductManager



class ProductModel(BaseModel):
    title = models.CharField(max_length=128)
    definition = models.TextField()
    slug = models.CharField(max_length=128, unique=True)

    owner = models.ForeignKey(
                User,
                on_delete=models.CASCADE,
                related_name='owner'

        )

    category = models.ForeignKey(
                Category,
                on_delete=models.CASCADE,
                related_name='products'

        )

    main_features = models.ManyToManyField(
            MainFeatureType,
            related_name='features'
    )
    sub_features = models.ManyToManyField(
            SubFeatureType,
            related_name='sub_features'
    )
    pictures = models.ManyToManyField(
            ProductImage,
            related_name='images'
    )


    ratings = models.DecimalField(max_digits=6,decimal_places=2,default=float(0))

    price_without_sale = models.IntegerField(default=0)
    price_in_sale = models.IntegerField(default=0)
    currency = models.CharField(max_length=128)

    is_sale = models.BooleanField(default=False)
    is_credit_for = models.BooleanField(default=False)

    objects = ProductManager()



    def update_ratings(self):

        self.ratings = self.objects.aggregate(Avg(str('comments__rating')))
        self.ratings.save()

    class Meta:
        ordering = ("id",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self) -> str:
        return self.title








