from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Heroes, Villains, Side_characters
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

class HeroesListView(ListView):
    template_name = 'characters/heroes/hero_list.html'
    model = Heroes


class HeroDetailView(DetailView):
    template_name = 'characters/heroes/hero_detail.html'
    model = Heroes


class HeroesUpdateView(UpdateView):
    template_name = 'characters/heroes/heroes_update.html'
    model = Heroes
    fields = ('real_name', 'superhero_name', 'male', 'powers', 'bio', 'short_info',)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class HeroesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'characters/heroes/heroes_create.html'
    fields = ('real_name', 'superhero_name', 'male', 'powers', 'bio', 'short_info', 'hero_img')
    model = Heroes
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class HeroDeleteView(DeleteView):
    template_name = 'characters/heroes/heroes_delete.html'
    model = Heroes
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class VillainsListView(ListView):
    template_name = 'characters/villains/villains_list.html'
    model = Villains


class VillainsDetailView(DetailView):
    template_name = 'characters/villains/villains_detail.html'
    model = Villains


class VillainsUpdateView(UpdateView):
    template_name = 'characters/villains/villains_update.html'
    model = Villains
    fields = ('real_name', 'villiain_name', 'male', 'powers', 'bio', 'short_info')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class VillainsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'characters/villains/villains_create.html'
    fields = ('real_name', 'villiain_name', 'male', 'powers', 'bio', 'short_info', 'vl_img')
    model = Villains
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VillainsDeleteView(DeleteView):
    template_name = 'characters/villains/villains_delete.html'
    model = Villains
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class SideListView(ListView):
    template_name = 'characters/side/side_list.html'
    model = Side_characters


class SideDetailView(DetailView):
    template_name = 'characters/side/side_detail.html'
    model = Side_characters


class SideUpdateView(UpdateView):
    template_name = 'characters/side/side_update.html'
    model = Side_characters
    fields = ('name', 'full_name', 'attitude', 'info')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class SideCreateView(LoginRequiredMixin, CreateView):
    template_name = 'characters/side/side_create.html'
    fields = ('name', 'full_name', 'attitude', 'info', "side_img")
    model = Side_characters
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SideDeleteView(DeleteView):
    template_name = 'characters/side/side_delete.html'
    model = Side_characters
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class SearchHeroesListView(ListView):
    model = Heroes
    context_object_name = 'search_list'
    template_name = 'characters/searchH_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Heroes.objects.filter(
            Q(superhero_name__icontains=query) | Q(real_name__icontains=query)

        )


