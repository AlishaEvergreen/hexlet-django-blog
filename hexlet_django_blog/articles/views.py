from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DetailView
from .models import Article
from .forms import ArticleForm


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'app_name': 'Articles',
            'articles': articles,
        })

# А можно и так:
# class IndexView(ListView):
#     model = Article
#     template_name = 'articles/index.html'
#     context_object_name = 'articles'
#     queryset = Article.objects.all()[:15]

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['app_name'] = 'Articles'
#         return context


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/update.html'

    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.object.pk})


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/detail.html'
