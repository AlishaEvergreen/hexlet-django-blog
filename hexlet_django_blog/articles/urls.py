from django.urls import path
from hexlet_django_blog.articles import views

app_name = "articles"

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:pk>/update/', views.ArticleUpdate.as_view(), name='update'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
]
