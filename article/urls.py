from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ArticleList.as_view(), name='article-list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+).html$', views.ArticleDetail.as_view(), name='article-detail'),
    url(r'^tags/(?P<slug>[-\w]+)/$', views.TagDetail.as_view(), name='tag'),
    url(r'^(?P<hierarchy>.+)/$', views.TopicDetail.as_view(), name='topic'),
]

