from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),#name is actually getting used in appropriate place of base html href links
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), # blog/post_list.html <- <app>/<model>_<viewtype>.html
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),# blog/post_detail.html
    path('post/new/', PostCreateView.as_view(), name='post-create'),# blog/post_form.html
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('redirect_fb', views.redirect_fb, name='redirect_fb'),
    path('redirect_tw', views.redirect_tw, name='redirect_tw'),
    path('redirect_ig', views.redirect_ig, name='redirect_ig'),
    path('redirect_yt', views.redirect_yt, name='redirect_yt'),
]