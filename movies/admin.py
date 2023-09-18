from django.contrib import admin

from .models import Film, Comment

class CommentInLine(admin.StackedInline):
    model = Comment


class FilmAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Film, FilmAdmin)
admin.site.register(Comment)