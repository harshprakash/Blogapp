from django.contrib import admin
from django.urls import path,include
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('', PostListView.as_view(),name="home"),
    path('detail/<int:pk>/',PostDetailView.as_view(),name="detail"),
    path('create/new/',PostCreateView.as_view(),name="create"),
    path('<int:pk>/update/',PostUpdateView.as_view(),name="update"),
    path('<str:username>/',UserPostListView.as_view(),name="user-post"),
    
    
    path('<int:pk>/delete/',PostDeleteView.as_view(),name="delete"),
    
]
