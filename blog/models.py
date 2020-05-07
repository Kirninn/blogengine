from django.db import models
from django.shortcuts import reverse
from time import time
from django.utils.text import slugify

def gen_slug(any_item):
    new_slug = slugify(any_item, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    body = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts' )
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('url_post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('url_post_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('url_post_delete', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('url_tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('url_tag_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('url_tag_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
