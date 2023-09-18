from django.contrib import admin

from .models import Heroes, Villains, Side_characters

admin.site.register(Heroes)
admin.site.register(Villains)
admin.site.register(Side_characters)
