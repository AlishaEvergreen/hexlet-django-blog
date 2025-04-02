from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .models import Article
from .forms import ArticleForm


class IndexView(ListView):
    model = Article
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'Articles'
        context["articles"] = Article.objects.all()
        return context


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/update.html'
    success_url = reverse_lazy('articles:articles_index')
