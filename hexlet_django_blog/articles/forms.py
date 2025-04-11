from django.forms import ModelForm

from .models import Article, ArticleComment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': ''})
        self.fields['content'].widget.attrs.update({'placeholder': ''})


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment  # Указываем, какая модель лежит в основе
        fields = ['content']  # Какие поля модели включаем в форму
