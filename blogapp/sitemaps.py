from django.contrib.sitemaps import Sitemap
from .models import Post
from taggit.models import Tag
from django.urls import reverse

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
       return Post.published.all()

    def lastmod(self, obj):
       return obj.updated




class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Tag.objects.all()

    def location(self, obj):
        return reverse('blog:post_list_by_tag', args=[obj.slug])