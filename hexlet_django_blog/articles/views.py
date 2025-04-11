from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ArticleCommentForm, ArticleForm
from .models import Article


class SuccessMessageMixin:
    success_msg = ""

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_msg:
            messages.success(
                self.request, self.success_msg.format(obj=self.object)
            )
        return response


class IndexView(ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'


class ArticleCreate(SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/create.html"
    success_msg = "Статья '{obj.title}' успешно создана"

    def get_success_url(self):
        return self.object.get_absolute_url()


class ArticleUpdate(SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/update.html'
    success_msg = "Статья '{obj.title}' успешно обновлена"

    def get_success_url(self):
        return self.object.get_absolute_url()


class ArticleDelete(SuccessMessageMixin, DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_msg = "Статья '{obj.title}' успешно удалена"
    success_url = reverse_lazy("articles:index")


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleCommentForm()
        context['comments'] = self.object.articlecomment_set.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ArticleCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.save()
            return redirect('articles:detail', pk=self.object.pk)

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


# А можно и так (используем только View)

# from django.views import View
# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse, reverse_lazy
# from django.contrib import messages

# from .models import Article
# from .forms import ArticleForm, ArticleCommentForm


# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.all()
#         return render(request, 'articles/index.html', {'articles': articles})


# class ArticleCreate(View):
#     def get(self, request, *args, **kwargs):
#         form = ArticleForm()
#         return render(request, "articles/create.html", {"form": form})

#     def post(self, request, *args, **kwargs):
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save()
#             messages.success(
#                 request, f"Статья '{article.title}' успешно создана"
#             )
#             return redirect(article.get_absolute_url())
#         return render(request, "articles/create.html", {"form": form})


# class ArticleUpdate(View):
#     def get(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         form = ArticleForm(instance=article)
#         return render(
#             request,
#             'articles/update.html',
#             {"form": form, "article": article}
#         )

#     def post(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         form = ArticleForm(request.POST, instance=article)
#         if form.is_valid():
#             article = form.save()
#             messages.success(
#                 request, f"Статья '{article.title}' успешно обновлена"
#             )
#             return redirect(article.get_absolute_url())
#         return render(
#             request,
#             'articles/update.html',
#             {"form": form, "article": article}
#         )


# class ArticleDelete(View):
#     def get(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         return render(request, "articles/delete.html", {"article": article})

#     def post(self, request, *args, **kwargs):
#         article_pk = kwargs.get('pk')
#         article = get_object_or_404(Article, pk=article_pk)
#         messages.success(request, f"Статья '{article.title}' успешно удалена")
#         article.delete()
#         return redirect(reverse_lazy("articles:articles_index"))


# class ArticleDetail(View):
#     def get(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         form = ArticleCommentForm()
#         comments = article.articlecomment_set.all()
#         return render(
#             request,
#             'articles/detail.html',
#             {"article": article, "form": form, "comments": comments}
#         )

#     def post(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         form = ArticleCommentForm(request.POST)
#         comments = article.articlecomment_set.all()

#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.article = article
#             comment.save()
#             return redirect(article.get_absolute_url())

#         return render(
#             request,
#             'articles/detail.html',
#             {"article": article, "form": form, "comments": comments}
#         )
