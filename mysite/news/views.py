from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
import news
from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News  # получаем все данные с модели News
    template_name = 'news/home_news_list.html'  # Выбор дефолтного файла в замен news_list.html
    context_object_name = 'news'
    extra_context = {'title': 'Главная'}  # Название в шапке сайта

    def get_context_data(self, *, object_list=None, **kwargs):  # Название в шапке сайта
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    
    def get_queryset(self):  # получение отфильтрованного списка новостей, отфильтрованного по наличию публикации
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False  # Запретить показ пустых списков
    
    def get_context_data(self, *, object_list=None, **kwargs):  # Название в шапке сайта
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):  # получение отфильтрованного списка новостей, отфильтрованного по теме
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # template_name = 'news/news_detail.html' изменение дефолтного шаблона на другой


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#
#     }
#     return render(request, template_name='news/index.html', context=context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)  # get_object возвращает заглушку при неправильном адресе
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':  # Если данные отправили из формы на сайт, то выполнить условие
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news_new = News.objects.create(**form.cleaned_data) # Сохранение в БД
            news_new = form.save()
            return redirect(news_new)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
