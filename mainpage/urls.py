from django.urls import path
from . import views
urlpatterns=[
    path('post/',views.mainpage_all,name='post'),
    path('post/<int:id>/', views.detail, name='show_detail'),
    path('add-post/', views.PostCreate.as_view(), name='add-post'),
    path('post/<int:id>/update/', views.PostUpdate.as_view(), name='show_detail'),
    path('post/<int:id>/delete/', views.PostDelete.as_view(), name='show_detail'),
    path('posts/', views.Post.as_view(), name='posts'),
    path('posts-2/', views.PostDetail.as_view(), name='posts-2'),
]