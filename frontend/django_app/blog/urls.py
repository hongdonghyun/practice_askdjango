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
    url(r'^(?P<post_pk>\d+)/comment_new/$', views.CommentCreateView.as_view(), name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit$', views.CommentEditView.as_view(), name='comment_edit'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete$', views.CommentDeleteView.as_view(), name='comment_delete'),

]
