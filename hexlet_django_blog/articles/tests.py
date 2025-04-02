from django.test import TestCase
from django.urls import reverse
from .models import Article


class ArticlesTest(TestCase):
    def setUp(self):
        # Создаем тестовую статью в базе данных перед выполнением тестов
        self.article = Article.objects.create(
            title="Test Article",
            content="Test Content"
        )

    def test_articles_list(self):
        response = self.client.get(reverse("articles:articles_index"))
        self.assertEqual(response.status_code, 200)

        # Проверяем наличие данных в контексте шаблона
        self.assertIn('articles', response.context)
        articles = response.context['articles']

        # Проверяем не пустой ли список статей
        self.assertTrue(len(articles) > 0)

    def test_update_article(self):
        article_id = self.article.pk

        update_data = {
            'title': 'Updated Title',
            'content': 'Updated Content'
        }

        response = self.client.post(
            reverse('articles:update', kwargs={'pk': article_id}),
            data=update_data
        )

        # Обновляем объект статьи из базы данных
        self.article.refresh_from_db()

        # Проверяем редирект (обычно 302 для успешного обновления)
        self.assertEqual(response.status_code, 302)

        # Проверяем, что данные статьи изменились
        self.assertEqual(self.article.title, "Updated Title")
        self.assertEqual(self.article.content, "Updated Content")
