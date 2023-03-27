from django.urls import resolve, reverse

from recipes import views

from .teste_recipe_base import recipeTestBase


# Render tests
class RecipeViewsTest(recipeTestBase):

    def test_recipe_home_views_function_is_correct(self):
        view_home = resolve('/')
        self.assertIs(view_home.func, views.home)

    # testa resposta http 200=ok
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    # testa load do template
    def test_recipe_home_view_loads_correct_templat(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # teste home template quando não ha receita
    def test_recipe_home_template_shows_no_recipe_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8')
            )

    # teste de home quando ha conteúdo, criando receita aqui
    def test_recipe_home_template_loads_recipes(self):
        # Need recipe for this test
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        # Verifica se as strings estão no template da receita criada
        self.assertIn('Recipe Title', content)
        self.assertIn('10 min', content)
        self.assertIn('5 cups', content)
        # verifica se 1 receita foi criada
        self.assertEqual(len(response_context_recipes), 1)

    # testa view
    def test_recipe_category_views_function_is_correct(self):
        view_category = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
            )
        self.assertIs(view_category.func, views.category)

    # testa retorno 404 se não ha receita encontrada
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    # testa pagina da receita
    def test_recipe_detail_views_function_is_correct(self):
        view_detail = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
            )
        self.assertIs(view_detail.func, views.recipe)

    # testa retorno 404 se pagina não foi encontrada
    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 10000})
        )
        self.assertEqual(response.status_code, 404
                         )
