from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SuperHeroChangeForm, SuperHeroCreationForm
from .models import SuperHeroUser

class SuperheroUserAdmin(UserAdmin):
    add_form = SuperHeroCreationForm
    form = SuperHeroChangeForm
    model = SuperHeroUser
    list_display = ['username', 'age', 'superhero_name']

admin.site.register(SuperHeroUser)