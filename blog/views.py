from .models import News, Comments
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.shortcuts import redirect, render
from .forms import CommentsForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

class NewsListView(ListView):
    template_name = 'news/news_list.html'
    model = News


class NewsDetailView(DetailView):
    template_name = 'news/news_detail.html'
    model = News


class NewsUpdateView(UpdateView):
    template_name = 'news/news_update.html'
    model = News
    fields = ('title', 'text')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class NewsCreateView(LoginRequiredMixin,  CreateView):
    template_name = 'news/news_create.html'
    fields = ('title', 'text', "news_img")
    model = News
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class AddComment(CreateView):
    template_name = 'add_comment.html'
    form_class = CommentsForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)