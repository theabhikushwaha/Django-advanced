from django.test import TestCase
from django.urls import reverse

from .models import Article

# Create your tests here.



class ArticleModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.article = Article.objects.create(title="Hello")

    def test_str(self):
        self.assertEqual(str(self.article), "Hello")


class ArticleViewTests(TestCase):
    def test_list_view_returns_200(self):
        resp = self.client.get(reverse("article-list"))
        self.assertEqual(resp.status_code, 200)