from django.urls import path
from hexlet_django_blog.article import views

app_name = "articles"

urlpatterns = [
    path('', views.ArticleIndexView.as_view(), name='articles_index'),
    path('<str:tags>/<int:article_id>/', views.ArticleDetailView.as_view(),
         name='article'),
]
