from django.contrib import admin

from .models import News, Comments

class CommentsInLine(admin.StackedInline):
    model = Comments


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        CommentsInLine,
    ]


admin.site.register(News, NewsAdmin)
admin.site.register(Comments)