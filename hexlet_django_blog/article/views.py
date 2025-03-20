from django.shortcuts import render
from django.views import View


class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'articles/index.html', context={
            'app_name': 'Articles',
        })
