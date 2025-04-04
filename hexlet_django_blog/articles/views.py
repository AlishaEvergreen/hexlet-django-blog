# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView
from .models import Article
from .forms import ArticleForm


class IndexView(ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by("id")[:15]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = 'Articles'
        return context


# А можно и так:
# class IndexView(View):

#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()[:15]
#         return render(request, 'articles/index.html', context={
#             'app_name': 'Articles',
#             'articles': articles,
#         })


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/update.html'

    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.object.pk})


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/detail.html'


# А можно и так:
# class ArticleDetail(View):
#     def get(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs['pk'])
#         return render(request, 'articles/detail.html', context={
#             'article': article,
#         })
