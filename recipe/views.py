from django.shortcuts import render, redirect
from .models import *
from .forms import RecipeForm
from django.views.generic import ListView


class Index(ListView):
    model = Recipe
    template_name = 'recipe/index.html'
    context_object_name = 'recipe'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Книга рецептов'
        return context

    def get_queryset(self):
        return Recipe.objects.filter(published=True)


def index(request):
    recipe = Recipe.objects.filter(published=True)
    context = {
        'recipe': recipe,
        'title': 'Список рецептов',
        'categories': Category.objects.all(),
    }
    return render(request, 'recipe/index.html', context=context)


def recipe_view(request, recipe_slug):
    recipe_full = Recipe.objects.get(slug=recipe_slug)
    context = {
        'recipe_full': recipe_full,
        'tags': recipe_full.tags.all(),
    }
    return render(request, 'recipe/recipe.html', context=context)


# class Tag(ListView):
#     model = Recipe
#     template_name = 'recipe/tag.html'
#     context_object_name = 'recipe'
#
#     def get_queryset(self):
#         # tag = Tag.objects.get(slug=self.kwargs['tag_slug'])
#         return Recipe.objects.filter(published=True)


def tag_view(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    context = {
        'recipe': tag.recipe_set.all(),
        'title': tag.title,
    }
    return render(request, 'recipe/tag.html', context=context)


# class Cat(ListView):
#     model = Recipe
#     template_name = 'recipe/category.html'
#     context_object_name = 'recipe'
#
#     def get_queryset(self):
#         return Recipe.objects.filter(category=self.kwargs['category_slug'], published=True)


def category_view(request, category_slug):
    cat = Category.objects.get(slug=category_slug)
    context = {
        'recipe': cat.recipe_set.all(),
        'title': cat.title,
    }
    return render(request, 'recipe/category.html', context=context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # recipe = Recipe.objects.create(**form.cleaned_data)
            recipe = form.save()
            return redirect(recipe)
    else:
        form = RecipeForm()
    return render(request, 'recipe/add_recipe.html', {'form': form})


def about(request):
    return render(request, 'recipe/about.html')