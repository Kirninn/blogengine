from django.urls import path


from .views import *

urlpatterns = [
    path('', post_list, name='url_blog_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='url_post_detail'),
    path('tags/', tags_list, name='url_tags_list'),
    path('tags/create/', TagCreate.as_view(), name='url_tag_create'),
    path('tags/<str:slug>/', TagDetail.as_view(), name='url_tag_detail'),
]
