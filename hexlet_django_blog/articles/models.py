from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=55, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE,
        default=1,
    )
    content = models.CharField('content', max_length=10)
