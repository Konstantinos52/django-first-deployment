from django.conf.urls import url
from . import views
app_name= 'post'

urlpatterns = [
    url(r'^all_posts/$', views.PostList.as_view(),  name=  'post_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name = 'post_detail'),
    url(r'^add_a_post/$', views.CreatePostView.as_view(), name= 'create'),
    url(r'^(?P<pk>[0-9]+)/change/$', views.UpdatePostView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeletePostView.as_view(), name='delete'),
    url(r'^(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='comment'),
    url(r'^(?P<pk>[0-9]+)/comment_remove/$', views.comment_remove, name='comment_remove'),
]












































