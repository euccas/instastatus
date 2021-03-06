"""insta2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from insta2.views import TestView, PostsView, PostDetailView, PostCreateView, PostEditView, PostDeleteView

urlpatterns = [
  path('test/', TestView.as_view(), name="test"),
  path('posts/', PostsView.as_view(), name="posts"),
  path('post/<int:pk>/', PostDetailView.as_view(), name="post"),
  path('post/new/', PostCreateView.as_view(), name="create_post"),
  path('post/edit/<int:pk>/', PostEditView.as_view(), name="edit_post"),
  path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="delete_post")
]