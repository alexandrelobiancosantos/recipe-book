from django.test import TestCase

from recipes.models import Category, Recipe, User


class recipeTestBase(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='Category')  # ou
        # category = Category(name='category')
        # category.full_clean()
        # category.save()
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123@123',
            email='user@123',
            )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='min',
            servings=5,
            servings_unit='cups',
            preparation_steps='Recipe Prep. Steps',
            preparation_step_in_html=False,
            is_published=True,
        )
        return super().setUp()
