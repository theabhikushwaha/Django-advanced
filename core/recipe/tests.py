from django.test import TestCase
from django.urls import reverse


class RecipeMessageTests(TestCase):
    def test_success_message_is_shown_on_recipe_home(self):
        response = self.client.post(
            reverse('recipe_form'),
            {
                'user_name': 'Abhi',
                'recipe_name': 'Test recipe',
                'ingredients': 'Flour',
                'description': 'Mix and cook.',
            },
            follow=True,
        )

        self.assertRedirects(response, reverse('recipehome'))
        self.assertContains(response, 'Recipe added.')
