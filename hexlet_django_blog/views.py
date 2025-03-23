from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy("article", args=["python", 42]))


def about(request):
    context = {'tags': ['Python', 'Django', 'Web']}
    return render(request, 'about.html', context)
