from django.conf.urls import url

from blog import views

urlpatterns = [
    # post
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    # comment
    url(r'^(?P<pk>\d+)/comment_new/$', views.comment_new, name='comment_new'),

]
