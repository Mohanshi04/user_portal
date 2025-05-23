from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),                        # For patients
    path('my-posts/', views.my_posts, name='my_posts'),                # Doctor's own posts
    path('create/', views.create_post, name='create_post'),            # Create new blog post
]
