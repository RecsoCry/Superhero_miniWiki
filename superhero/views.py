from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import SuperHeroCreationForm, SuperHeroChangeForm
from .models import SuperHeroUser


class SignUpView(CreateView):
    form_class = SuperHeroCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')


class ProfileView(DetailView):
    model = SuperHeroUser
    template_name = "profile.html"


class ChangeProfileView(UpdateView):
    model = SuperHeroUser

    template_name = 'profile_edit.html'
    fields = ('username', 'email', 'first_name', 'last_name',  'age')
    success_url = reverse_lazy('home')
