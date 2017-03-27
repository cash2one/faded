from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from taggit.models import Tag
from .models import Topic, Article


class ArticleDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context


class ArticleList(ListView):
    queryset = Article.published.all()
    context_object_name = 'articles'
    paginate_by = 3


class TopicDetail(ListView, SingleObjectMixin):
    context_object_name = 'articles'
    paginate_by = 3
    template_name = 'article/topic_detail.html'

    def get(self, request, *args, **kwargs):
        self.kwargs['slug'] = self.kwargs.get('hierarchy').split('/')[-1]
        self.object = self.get_object(queryset=Topic.objects.all())
        return super(TopicDetail, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.article_set(manager='published').all()

    def get_context_data(self, **kwargs):
        context = super(TopicDetail, self).get_context_data(**kwargs)
        context['topic'] = self.object
        context['meta'] = self.object.as_meta(self.request)
        return context


class TagDetail(ListView, SingleObjectMixin):
    context_object_name = 'articles'
    paginate_by = 3
    template_name = 'article/tag_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Tag.objects.all())
        return super(TagDetail, self).get(request, *args, **kwargs)

    def get_queryset(self):
        print(self.object)
        return Article.published.filter(self.object)

    def get_context_data(self, **kwargs):
        context = super(TagDetail, self).get_context_data(**kwargs)
        context['tag'] = self.object
        return context
