from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView  # заимствуем этот клас для динамической страницы


def news_home(reqest):
    news = Article.objects.order_by('-data')
    return render(reqest, 'news/news_home.html', {'news': news}) # отсюда можно сделать запрос на любой html из templates

class newsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'news/news_delete.html'

class newsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm

class newsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


def create(reqest):
    error = ''
    if reqest.method == 'POST':
        form = ArticleForm(reqest.POST)  # берет данные из форм
        if form.is_valid():  # проверка что все данные заполнены. метод из ModelForm из заимственного класса
            form.save()  # сохраняем новую запись
            return redirect('./')  # перекидвает на домашнюю страницу
        else:
            error = 'Форма была не верной'

    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }

    return render(reqest, 'news/create.html', data)


