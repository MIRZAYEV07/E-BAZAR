from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "name")
    list_display_links = ("title",)
    search_fields = ["title"]


admin.site.register(Category, CategoryAdmin)

# Register your models here.
