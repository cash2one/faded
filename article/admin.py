from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Topic, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'author', 'status', 'publish')
    list_filter = ('status', 'topic', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()


@admin.register(Topic)
class TopicAdmin(MPTTModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
