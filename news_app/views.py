from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from .models import NewsModel, CategoryModel


class News_list_View(ListView):
    model = NewsModel
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()
        context["news_list"] = NewsModel.published.all().order_by('-published_time')[:5]
        context['business_news'] =NewsModel.published.all().filter(category__name='Business').order_by('-published_time')[:5]
        context['fashion_news'] = NewsModel.published.all().filter(category__name='Fashion').order_by('-published_time')[:5]
        context['technology_news'] = NewsModel.published.all().filter(category__name='Technology').order_by('-published_time')[:5]
        context['photography_news'] = NewsModel.published.all().filter(category__name='Photography').order_by('-published_time')[:6]
        context['sport_news'] = NewsModel.published.all().filter(category__name='Sports').order_by('-published_time')[:5]
        context['life_style_news'] = NewsModel.published.all().filter(category__name='Life & Style').order_by('-published_time')[
                                :5]
        context['games_news'] = NewsModel.published.all().filter(category__name='Games').order_by('-published_time')[:5]

        return context

def news_list_View(request):
    news_list = NewsModel.published.all()
    category = CategoryModel.objects.all()
    context = {
        'news_list': news_list,
        "category": category
    }
    return render(request,'news/news_list.html', context)
def news_detail(request, id):
    # id ni urniga news yozuldi
    news_detail = get_object_or_404(NewsModel,
                                    slug=id,
                                    status=NewsModel.Status.Published) # id=id urniga slug=news yozildi
    context = {
        "news_detail": news_detail,

    }
    return render(request, 'news/news_detail.html', context)
class TechnologyNewsView(ListView):
    model = NewsModel
    template_name = 'news/technology.html'
    context_object_name = 'technology'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Technology')
        return news

class FashionNewsView(ListView):
    model = NewsModel
    template_name = 'news/fashion.html'
    context_object_name = 'fashion'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Fashion')
        return news
class GamesNewsView(ListView):
    model = NewsModel
    template_name = 'news/games.html'
    context_object_name = 'games'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Games')
        return news
class Lifi_styleNewsView(ListView):
    model = NewsModel
    template_name = 'news/life_style.html'
    context_object_name = 'life_style'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Life & Style')
        return news
class PhotographyNewsView(ListView):
    model = NewsModel
    template_name = 'news/photography.html'
    context_object_name = 'photo'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Photography')
        return news

class BusinessNewsView(ListView):
    model = NewsModel
    template_name = 'news/business.html'
    context_object_name = 'business'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Business')
        return news
class SportNewsView(ListView):
    model = NewsModel
    template_name = 'news/sports.html'
    context_object_name = 'sport'
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sports')
        return news

class NewsUpdateView(UpdateView):
    model = NewsModel
    fields = ['title', 'slug', 'body', 'image', 'category', 'status']
    template_name = 'crud/news_edit.html'
    success_url = reverse_lazy('all_news_list')




class NewsDeleteView(DeleteView):
    model = NewsModel
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('all_news_list')