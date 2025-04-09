# from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .models import Article
from .forms import ArticleForm, ArticleCommentForm


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


class ArticleCreate(SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/create.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f"Статья '{self.object.title}' успешно создана"
        )
        return response

    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.object.pk})


# А можно и так:
# class ArticleFormCreateView(View):

#     def get(self, request, *args, **kwargs):
#         form = ArticleForm()
#         return render(request, 'articles/create.html', {'form': form})


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/update.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f"Статья '{self.object.title}' успешно обновлена"
        )
        return response

    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.object.pk})


# class ArticleDetail(DetailView):
#     model = Article
#     template_name = 'articles/detail.html'


# А можно и так:
# class ArticleDetail(View):
#     def get(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs['pk'])
#         return render(request, 'articles/detail.html', context={
#             'article': article,
#         })


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        # Получаем стандартный контекст от родителя
        context = super().get_context_data(**kwargs)

        # Добавляем в контекст пустую форму комментария
        context['form'] = ArticleCommentForm()

        # Получаем все комментарии, связанные с текущей статьей
        context['comments'] = self.object.articlecomment_set.all()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Получаем текущую статью по pk из URL

        # Заполняем форму данными из POST-запроса
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            # Создаём объект комментария, но пока не сохраняем его в БД
            comment = form.save(commit=False)

            # Указываем, к какой статье относится этот комментарий
            comment.article = self.object

            # Сохраняем комментарий в базу данных
            comment.save()

            # Перенаправляем пользователя обратно на страницу статьи
            return redirect('articles:detail', pk=self.object.pk)

        # Если форма невалидна, возвращаем страницу с ошибками формы
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy("articles:articles_index")
    template_name = "articles/delete.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f"Статья '{self.object.title}' успешно удалена"
        )
        return response

# А можно и так:
# class ArticleDelete(View):

#     def post(self, request, *args, **kwargs):
#         article_id = kwargs.get('pk')
#         article = Article.objects.get(id=article_id)
#         if article:
#             article.delete()
#         return redirect('articles:articles_index')
