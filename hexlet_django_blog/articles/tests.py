from django.urls import reverse
from django.test import TestCase
from .models import Article


class ArticlesTest(TestCase):
    def setUp(self):
        # Создаем тестовую статью в базе данных перед выполнением тестов
        self.article = Article.objects.create(
            title="Test Article",
            content="Test Content"
        )

    def assertArticle(self, article, article_data):
        self.assertEqual(article.__str__(), article_data["title"])
        self.assertEqual(article.title, article_data["title"])
        self.assertEqual(article.content, article_data["content"])

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

        # Проверяем редирект после обновления
        self.assertRedirects(
            response, reverse("articles:detail", kwargs={'pk': article_id})
        )

        # Делаем GET-запрос, чтобы получить страницу с детальной информацией
        response = self.client.get(
            reverse('articles:detail', kwargs={'pk': article_id})
        )

        # Получаем статью из контекста шаблона
        article_from_context = response.context['article']

        # Проверяем, что данные в контексте соответствуют обновлённым
        self.assertEqual(article_from_context.title, update_data['title'])
        self.assertEqual(article_from_context.content, update_data['content'])

        # Также можно дополнительно проверить отображение текста в HTML
        self.assertContains(response, update_data['title'])
        self.assertContains(response, update_data['content'])
