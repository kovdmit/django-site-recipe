from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('recipe/<str:recipe_slug>/', recipe_view, name='recipe_view'),
    path('tag/<str:tag_slug>/', tag_view, name='tag_view'),
    path('category/<str:category_slug>/', category_view, name='category_view'),
    path('about/', about, name='about'),
    path('add_recipe/', add_recipe, name='add_recipe'),
]