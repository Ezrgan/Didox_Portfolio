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

class CategoryExample(models.Model):
    category = models.ForeignKey(Category, related_name='examples', on_delete=models.CASCADE, verbose_name=_("Category"))
    image = CloudinaryField('image', folder='category_examples')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Category Example")
        verbose_name_plural = _("Category Examples")
        ordering = ['created_at']

class Project(models.Model):
    description = models.CharField(max_length=200, verbose_name=_("Admin Description"), blank=True)
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

# --- MODELO DE PERFIL (SOLUCIÓN DEFINITIVA) ---

class UserProfile(models.Model):
    # Estado del Freelancer
    is_open_for_work = models.BooleanField(
        default=True, 
        verbose_name=_("Is Open for Work?"), 
        help_text=_("Desmarcar para mostrar estado 'Fully Booked'.")
    )

    full_name = models.CharField(max_length=150, verbose_name=_("Full Name"))
    profile_image = CloudinaryField('image', folder='profile', blank=True, null=True)
    
    # Ubicación Única
    location = models.CharField(max_length=100, verbose_name=_("Location"), default="Cuba")
    
    # Biografía (Idiomas separados)
    bio_es = models.TextField(verbose_name=_("Biography (Spanish)"), help_text=_("Puedes incluir tu edad aquí manualmente."))
    bio_en = models.TextField(verbose_name=_("Biography (English)"))

    # Skills Únicas
    skills = models.TextField(verbose_name=_("Skills"), help_text=_("Lista separada por comas. Ej: After Effects, Blender, Nuke"))

    # Contacto Obligatorio
    whatsapp = models.CharField(max_length=20, verbose_name=_("WhatsApp Number"), help_text=_("Obligatorio. Incluir código país: +53..."))
    discord = models.CharField(max_length=100, verbose_name=_("Discord UserID"), help_text=_("Obligatorio."))

    # Redes Sociales Opcionales
    freelance = models.URLField(verbose_name=_("Freelance URL"), blank=True, null=True, help_text=_("Link a Upwork, Fiverr, etc."))
    instagram = models.URLField(verbose_name=_("Instagram URL"), blank=True, null=True)
    twitter = models.URLField(verbose_name=_("Twitter/X URL"), blank=True, null=True)
    facebook = models.URLField(verbose_name=_("Facebook URL"), blank=True, null=True)
    linkedin = models.URLField(verbose_name=_("LinkedIn URL"), blank=True, null=True)
    youtube = models.URLField(verbose_name=_("YouTube URL"), blank=True, null=True)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profile")

    def __str__(self):
        return self.full_name

    # Método helper para el template
    def get_skills_list(self):
        return [s.strip() for s in self.skills.split(',')] if self.skills else []