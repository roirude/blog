from django.contrib import admin
from django.contrib.admin import ModelAdmin

from article.models import Category, Article


admin.site.register(Category)

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ("name", "category", "author")
    search_fields = ("name",)
    list_filter = ("name", "author", "category")