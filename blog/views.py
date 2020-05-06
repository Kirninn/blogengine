from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Tag
from django.views.generic import View
from .utils import *
from .forms import TagForm, PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'


class TagUpdate(ObjectUpdateMixin,View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'


class PostUpdate(ObjectUpdateMixin,View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'
