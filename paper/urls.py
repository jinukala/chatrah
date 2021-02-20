from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.postlist.as_view(), name='posts'),
    path('post/<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
    path('post/amp/<slug:slug>/', views.postdetailamp.as_view(), name='post_detail_amp'),
]