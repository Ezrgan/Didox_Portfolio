from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description_en = models.TextField(verbose_name=_("Description (English)"), blank=True, null=True)
    description_es = models.TextField(verbose_name=_("Description (Spanish)"), blank=True, null=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Minimum Price"))
    is_gfx = models.BooleanField(default=False, verbose_name=_("Is GFX Category"), help_text=_("Check this if the category contains static images (no video, no links)."))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


    def __str__(self):
        return self.name

    @property
    def description(self):
        # Fallback for code that still accesses .description (optional, but good for safety)
        # However, user wants explicit language switching.
        return self.description_en

class CategoryExample(models.Model):
    category = models.ForeignKey(Category, related_name='examples', on_delete=models.CASCADE, verbose_name=_("Category"))
    # Usamos CloudinaryField para optimización automática
    image = CloudinaryField('image', folder='category_examples')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Category Example")
        verbose_name_plural = _("Category Examples")
        ordering = ['created_at']

class Project(models.Model):
    description = models.CharField(max_length=200, verbose_name=_("Admin Description"), blank=True, help_text=_("Internal description for identifying the project in the admin panel."))
    # Usamos CloudinaryField para optimización automática
    thumbnail = CloudinaryField('image', folder='projects')
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    link = models.URLField(verbose_name=_("Project Link"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ['-created_at']

    def __str__(self):
        return self.description if self.description else f"Project {self.id}"

class SiteConfiguration(models.Model):
    is_open_for_work = models.BooleanField(
        default=True, 
        verbose_name=_("Is Open for Work?"), 
        help_text=_("Uncheck to show 'Fully Booked' status on the home page.")
    )

    class Meta:
        verbose_name = _("Site Configuration")
        verbose_name_plural = _("Site Configuration")

    def __str__(self):
        return str(_("Site Configuration"))

    def save(self, *args, **kwargs):
        if not self.pk and SiteConfiguration.objects.exists():
            # Force update the existing one if someone tries to create a new one via code
            # But normally we handle this in Admin
            return SiteConfiguration.objects.first().save(*args, **kwargs)
        return super(SiteConfiguration, self).save(*args, **kwargs)