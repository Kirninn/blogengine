from django.urls import path


from .views import *

urlpatterns = [
    path('', index, name='url_blog_list'),
    path('post/<str:slug>/', post_detail, name='url_post_detail'),
    path('tags/', tags_list, name='url_tags_list'),
    path('tags/<str:slug>/', tag_detail, name='url_tag_detail'),
]
