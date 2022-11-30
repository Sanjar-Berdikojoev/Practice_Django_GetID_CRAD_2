from django.urls import path
from . import views
urlpatterns=[
    path('posts/',views.mainpage_all,name='posts'),
    path('posts/<int:id>/', views.detail, name='show_detail'),
]