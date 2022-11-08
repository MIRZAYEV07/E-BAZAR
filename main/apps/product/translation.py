from main.apps.category.models import Category
from .models.product import ProductModel
from modeltranslation.translator import TranslationOptions, translator


class ProductTranslationOptions(TranslationOptions):
    fields = ('definition',)

translator.register(ProductModel, ProductTranslationOptions)