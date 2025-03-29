from django.test import TestCase
from django.urls import reverse
from .models import Article


class ArticlesTest(TestCase):
    def test_articles_list(self):
        Article.objects.create(title="Test Article", content="Test Content")

        response = self.client.get(reverse("articles:articles_index"))
        self.assertEqual(response.status_code, 200)

        # Проверяем наличие данных в контексте шаблона
        self.assertIn('articles', response.context)
        articles = response.context['articles']

        # Проверяем не пустой ли список статей
        self.assertTrue(len(articles) > 0)
