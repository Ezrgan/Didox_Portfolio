from django.contrib import admin
from .models import Category, Project, CategoryExample

class CategoryExampleInline(admin.TabularInline):
    model = CategoryExample
    extra = 1
    max_num = 5

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_price', 'is_gfx')
    search_fields = ('name',)
    inlines = [CategoryExampleInline]
    save_on_top = True

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')
    list_filter = ('categories',)
    filter_horizontal = ('categories',)

@admin.register(CategoryExample)
class CategoryExampleAdmin(admin.ModelAdmin):
    list_display = ('category', 'created_at')
