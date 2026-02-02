from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description_en = models.TextField(verbose_name=_("Description (English)"), blank=True, null=True)
    description_es = models.TextField(verbose_name=_("Description (Spanish)"), blank=True, null=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Minimum Price"))

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

class Project(models.Model):
    description = models.CharField(max_length=200, verbose_name=_("Admin Description"), blank=True, help_text=_("Internal description for identifying the project in the admin panel."))
    thumbnail = models.ImageField(upload_to='projects/', verbose_name=_("Thumbnail"))
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    link = models.URLField(verbose_name=_("Project Link"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ['-created_at']

    def __str__(self):
        return self.description if self.description else f"Project {self.id}"
