from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .feeds import LatestPostsFeed


app_name='Blog'

urlpatterns = [
    path('blog/',views.post_list, name='post_list'), #link za numeraciju iz view
    #path('blog/',views.PostListView.as_view(), name='post_list'), # link za numeraciju ponocu clase iz viewa postlistvies
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
            views.post_detail,
            name='post_detail'),
    path('<int:post_id>/share/',views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/',
            views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed')
] 