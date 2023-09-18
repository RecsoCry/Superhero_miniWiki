from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import SuperHeroUser

class SuperHeroCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SuperHeroUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'age', 'first_name', 'last_name')

class SuperHeroChangeForm(UserChangeForm):

    class Meta:
        model = SuperHeroUser
        fields = UserChangeForm.Meta.fields
        # fields = ('username', 'email', 'age', )