from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('',post_view,name='postsview'),
    path('like-unlike/',like_unlike_post,name='like-unlike-post')
]
