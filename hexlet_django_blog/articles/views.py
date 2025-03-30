from django.views.generic import ListView
from .models import Article


class IndexView(ListView):
    model = Article
    template_name = 'articles/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'Articles'
        context["articles"] = Article.objects.all()
        return context
