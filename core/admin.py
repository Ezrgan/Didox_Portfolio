from django.contrib import admin
from .models import Category, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_price')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')
    list_filter = ('categories',)
    filter_horizontal = ('categories',)
