from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from meta.models import ModelMeta
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Topic(ModelMeta, MPTTModel):
    name = models.CharField('名称', max_length=64)
    slug = models.SlugField('唯一标识', unique=True, max_length=100)
    description = models.TextField('简介', blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='child_set', verbose_name="父主题")
    thumb = models.ImageField('缩略图', upload_to='topic', blank=True)
    _metadata = {
        "title": "name",
        "description": "description",
    }

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = '主题'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        topics = self.get_ancestors(include_self=True)
        topic_path = topics.values_list('slug', flat=True)
        hierarchy = '/'.join(topic_path)
        return reverse('article:topic',
                       args=[
                           hierarchy
                       ])


class Article(ModelMeta, models.Model):
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '已发布')
    )
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()
    title = models.CharField('标题', max_length=256)
    slug = models.SlugField('唯一标识', unique=True, max_length=100)
    author = models.ForeignKey(User, editable=False, verbose_name='作者')
    topic = TreeForeignKey(Topic, blank=True, null=True, default=None, verbose_name='主题')
    thumb = models.ImageField('缩略图', upload_to='article', blank=True)
    body = RichTextField('内容')
    view_count = models.IntegerField(editable=False, default=0)
    publish = models.DateTimeField('发布时间', default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField('状态', max_length=10, choices=STATUS_CHOICES, default='draft')

    _metadata = {
        'title': 'title',
        'description': 'body'
    }

    class Meta:
        ordering = ('-publish', )
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article-detail',
                       args=[
                           self.publish.year,
                           self.publish.strftime('%m'),
                           self.publish.strftime('%d'),
                           self.slug
                       ])

