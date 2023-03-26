from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

# Render tests


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view_home = resolve('/')
        self.assertIs(view_home.func, views.home)

    def test_recipe_category_views_function_is_correct(self):
        view_category = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view_category.func, views.category)

    def test_recipe_detail_views_function_is_correct(self):
        view_detail = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view_detail.func, views.recipe)
