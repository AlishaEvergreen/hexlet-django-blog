from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def about(request):
    context = {'tags': ['Python', 'Django', 'Web']}
    return render(request, 'about.html', context)
