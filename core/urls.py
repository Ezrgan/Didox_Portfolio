from django.urls import path
from .views import HomeView, ProjectListView, CategoryDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
