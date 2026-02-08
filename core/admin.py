from django.contrib import admin
from .models import Category, CategoryExample, Project, UserProfile

class CategoryExampleInline(admin.TabularInline):
    model = CategoryExample
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryExampleInline]
    list_display = ('name', 'min_price', 'is_gfx')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_at')
    filter_horizontal = ('categories',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Evita que se creen múltiples perfiles
    def has_add_permission(self, request):
        # Si ya existe 1 objeto, no deja crear más
        return not UserProfile.objects.exists()

    fieldsets = (
        ('Status', {
            'fields': ('is_open_for_work',)
        }),
        ('Personal Info', {
            'fields': ('full_name', 'profile_image', 'location', 'skills')
        }),
        ('Biography', {
            'fields': ('bio_es', 'bio_en')
        }),
        ('Mandatory Contact', {
            'fields': ('whatsapp', 'discord')
        }),
        ('Social Networks (Optional)', {
            'fields': ('freelance', 'instagram', 'twitter', 'facebook', 'linkedin', 'youtube')
        }),
    )