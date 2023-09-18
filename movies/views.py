from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Film
from django.urls import reverse_lazy
from .forms import CommentsForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin


class FilmListView(ListView):
    template_name = 'film/film_list.html'
    model = Film


class FilmDetailView(DetailView):
    template_name = 'film/film_detail.html'
    model = Film

class FilmUpdateView(UpdateView):
    template_name = 'film/film_update.html'
    model = Film
    fields = ('title', 'year', 'rating', 'plot')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class FilmCreateView(LoginRequiredMixin, CreateView):
    template_name = 'film/film_create.html'
    model = Film
    fields = ('title', 'year', 'rating', 'plot', 'movie', 'movie_img')
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FilmDeleteView(DeleteView):
    template_name = 'film/film_delete.html'
    model = Film
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class AddComment(CreateView):
    template_name = 'film/film_comments.html'
    form_class = CommentsForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)