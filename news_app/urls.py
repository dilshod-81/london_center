from django.urls import path
from .views import news_list_View, news_detail, News_list_View, TechnologyNewsView, FashionNewsView, \
    GamesNewsView, Lifi_styleNewsView, PhotographyNewsView, BusinessNewsView, SportNewsView, NewsUpdateView, \
    NewsDeleteView

urlpatterns = [
    path('', News_list_View.as_view(), name='all_news_list'),
    #path('', news_list_View, name='all_news_list'),
    path('news/<slug:id>/', news_detail, name='news_detail'),
    path('technology/', TechnologyNewsView.as_view(), name='technology_page'),
    path('fashion/', FashionNewsView.as_view(), name='fashion_page'),
    path('games/', GamesNewsView.as_view(), name='games_page'),
    path('life-style/', Lifi_styleNewsView.as_view(), name='life_style_page'),
    path('photo/', PhotographyNewsView.as_view(), name='photo_page'),
    path('business/', BusinessNewsView.as_view(), name='business_page'),
    path('sport/', SportNewsView.as_view(), name='sport_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]