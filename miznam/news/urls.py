from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.newsDetailView.as_view(), name='news_detail'),      # так обозначаем динамичский параметр, as_view тк это класс
    path('<int:pk>/update', views.newsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.newsDeleteView.as_view(), name='news_delete')
]