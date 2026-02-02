import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_didox.settings')
django.setup()

from core.models import Category

# Define categories with English and Spanish descriptions
categories_data = [
    {
        "name": "Digital Animation",
        "description_en": "Bring your ideas to life with high-impact 2D and 3D animation. Specializing in character animation, motion graphics, and immersive storytelling that captures attention and conveys emotion.",
        "description_es": "Da vida a tus ideas con animación 2D y 3D de alto impacto. Especializado en animación de personajes, motion graphics y narración inmersiva que capta la atención y transmite emociones.",
        "min_price": 500.00
    },
    {
        "name": "Graphic Design",
        "description_en": "Strategic visual design that communicates your brand's essence. From logos and branding to marketing materials, I create clean, modern, and memorable visuals that stand out.",
        "description_es": "Diseño visual estratégico que comunica la esencia de tu marca. Desde logotipos y branding hasta materiales de marketing, creo visuales limpios, modernos y memorables que destacan.",
        "min_price": 300.00
    },
    {
        "name": "Video Editing",
        "description_en": "Professional video editing services that turn raw footage into compelling stories. Expertise in pacing, color grading, sound design, and visual effects to produce cinema-quality results.",
        "description_es": "Servicios profesionales de edición de video que convierten metraje sin procesar en historias convincentes. Experiencia en ritmo, etalonaje, diseño de sonido y efectos visuales para producir resultados de calidad cinematográfica.",
        "min_price": 400.00
    },
    {
        "name": "VFX Composition",
        "description_en": "Seamless integration of CGI and live-action footage. Whether it's removing objects, adding elements, or creating entirely new worlds, my VFX composition skills enhance reality.",
        "description_es": "Integración perfecta de CGI y metraje de acción real. Ya sea eliminando objetos, añadiendo elementos o creando mundos completamente nuevos, mis habilidades de composición VFX mejoran la realidad.",
        "min_price": 600.00
    },
]

def seed():
    print("Seeding categories...")
    # Optional: Clear existing categories if you want a fresh start, 
    # but be careful with ForeignKeys (Projects).
    # Since we removed the 'description' field, old data is gone anyway for that column.
    
    for item in categories_data:
        # Update or Create to preserve ID links if possible, but names match.
        category, created = Category.objects.update_or_create(
            name=item['name'],
            defaults={
                'description_en': item['description_en'],
                'description_es': item['description_es'],
                'min_price': item['min_price']
            }
        )
        status = "Created" if created else "Updated"
        print(f"{status}: {category.name}")
    
    print("Done.")

if __name__ == '__main__':
    seed()
