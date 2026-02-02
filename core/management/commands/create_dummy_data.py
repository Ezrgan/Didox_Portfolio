from django.core.management.base import BaseCommand
from core.models import Category, Project
from decimal import Decimal

class Command(BaseCommand):
    help = 'Creates dummy categories and projects for testing'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Project.objects.all().delete()
        Category.objects.all().delete()

        # Real Categories based on user input
        categories_data = [
            {"name": "Edición de video", "description": "Edición profesional y creativa para todo tipo de proyectos audiovisuales.", "min_price": Decimal("300.00")},
            {"name": "VFX", "description": "Efectos visuales de alto impacto y composición avanzada.", "min_price": Decimal("800.00")},
            {"name": "Motion Graphics", "description": "Animación gráfica dinámica para marcas y explainer videos.", "min_price": Decimal("500.00")},
            {"name": "Animación digital", "description": "Creación de mundos y personajes animados con técnicas modernas.", "min_price": Decimal("700.00")},
            {"name": "Diseño Gráfico", "description": "Identidad visual, banners, miniaturas y material promocional.", "min_price": Decimal("200.00")},
        ]

        categories_map = {}
        for cat_data in categories_data:
            cat = Category.objects.create(**cat_data)
            categories_map[cat.name] = cat
            self.stdout.write(self.style.SUCCESS(f'Created category: {cat.name}'))

        # Create dummy projects with random categories
        # Using placeholder images that look more "motion graphics" like if possible, or just colors
        projects_config = [
            {"link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "cats": ["Edición de video", "VFX"]},
            {"link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "cats": ["Motion Graphics"]},
            {"link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "cats": ["Animación digital"]},
            {"link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "cats": ["Diseño Gráfico"]},
            {"link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "cats": ["VFX", "3D"]}, # 3D isn't in the list anymore, replacing with VFX or Animación
            {"link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "cats": ["Edición de video", "Motion Graphics"]},
            {"link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "cats": ["Animación digital", "VFX"]},
            {"link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "cats": ["Diseño Gráfico", "Motion Graphics"]},
        ]

        for i, conf in enumerate(projects_config, 1):
            project = Project.objects.create(link=conf["link"])
            # Filter valid categories (handling potential key errors if I messed up the list)
            valid_cats = [categories_map[c] for c in conf["cats"] if c in categories_map]
            project.categories.set(valid_cats)
            self.stdout.write(self.style.SUCCESS(f'Created project {i}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created real data!'))
