from django.urls import path
from hexlet_django_blog.articles import views

app_name = "articles"

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('create/', views.ArticleCreate.as_view(), name='articles_create'),
    path(
        '<int:pk>/delete/',
        views.ArticleDelete.as_view(),
        name='delete'
    ),
    path('<int:pk>/update/', views.ArticleUpdate.as_view(), name='update'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
]
