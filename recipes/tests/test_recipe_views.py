from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views

# Render tests


# Render tests
class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view_home = resolve('/')
        self.assertIs(view_home.func, views.home)

    # testa resposta http 200=ok
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_templat(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipe_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8')
            )

    def test_recipe_category_views_function_is_correct(self):
        view_category = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
            )
        self.assertIs(view_category.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_views_function_is_correct(self):
        view_detail = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
            )
        self.assertIs(view_detail.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 10000})
        )
        self.assertEqual(response.status_code, 404
                         )
