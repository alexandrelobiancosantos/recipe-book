from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


# URL tests
class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipe_details_url_is_correct(self):
        recipe_url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(recipe_url, '/recipes/1/')


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
