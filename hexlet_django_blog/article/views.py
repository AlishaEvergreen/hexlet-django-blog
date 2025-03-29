from django.views.generic.base import TemplateView
from .models import Article


class ArticleIndexView(TemplateView):
    template_name = "articles/index.html"
    articles = Article.objects.all()
    extra_context = {"app_name": "Articles", 'articles': articles}


class ArticleDetailView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "app_name": "Articles",
            "article_id": kwargs["article_id"],
            "tags": kwargs["tags"]
        })
        return context
