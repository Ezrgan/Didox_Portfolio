from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from .models import Project, Category, SiteConfiguration

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get or create the site config (singleton-ish)
        config, created = SiteConfiguration.objects.get_or_create(pk=1)
        context['site_config'] = config
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'core/project_list.html'
    context_object_name = 'projects'
    paginate_by = 15

    def get_queryset(self):
        queryset = Project.objects.all().prefetch_related('categories')
        categories = self.request.GET.getlist('categories[]')
        if categories:
            queryset = queryset.filter(categories__id__in=categories).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def render_to_response(self, context, **response_kwargs):
        # Handle AJAX request for filtering
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            projects_data = []
            for project in context['projects']:
                projects_data.append({
                    'id': project.id,
                    'thumbnail_url': project.thumbnail.url if project.thumbnail else '',
                    'link': project.link,
                    'categories': [{'id': cat.id, 'name': cat.name} for cat in project.categories.all()],
                    'is_gfx': project.categories.first().is_gfx if project.categories.exists() else False
                })
            
            return JsonResponse({
                'projects': projects_data,
                'has_next': context['page_obj'].has_next() if context['page_obj'] else False,
                'has_previous': context['page_obj'].has_previous() if context['page_obj'] else False,
                'num_pages': context['paginator'].num_pages if context['paginator'] else 1,
                'current_page': context['page_obj'].number if context['page_obj'] else 1,
            })
        return super().render_to_response(context, **response_kwargs)

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'core/category_detail.html'
    context_object_name = 'category'
    slug_field = 'id' # Using ID for simplicity as slug wasn't strictly requested but better for URL
    slug_url_kwarg = 'pk' 
