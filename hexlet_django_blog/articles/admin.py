from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title', 'content']
    list_filter = (('created_at', DateFieldListFilter),)
