from django.urls import path
from .views import NewsListView, NewsDetailView, NewsUpdateView, NewsCreateView, AddComment
from . import views
urlpatterns = [
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('news_detail/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news_create/', NewsCreateView.as_view(), name='news_create'),
    path('news_update/<int:pk>/', NewsUpdateView.as_view(), name='news_update'),
    path('add_comment/<int:pk>/', AddComment.as_view(), name='add_comment'),


]