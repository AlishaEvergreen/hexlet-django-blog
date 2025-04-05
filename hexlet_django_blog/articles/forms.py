from django.forms import ModelForm
from .models import Article, ArticleComment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment  # Указываем, какая модель лежит в основе
        fields = ['content']  # Какие поля модели включаем в форму
