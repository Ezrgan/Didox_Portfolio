from django.contrib import admin
from .models import Category, Project, CategoryExample, SiteConfiguration

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

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
