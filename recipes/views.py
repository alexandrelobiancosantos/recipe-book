from django.shortcuts import render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        # 'recipes': [make_recipe() for _ in range(7)],
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
        ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        # 'recipes': [make_recipe() for _ in range(7)],
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
