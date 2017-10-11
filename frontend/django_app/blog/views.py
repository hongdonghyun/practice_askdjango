from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blog.models import Post, Comment

index = ListView.as_view(model=Post, template_name='blog/index.html')

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('index'))

post_new = CreateView.as_view(model=Post, fields='__all__')

comment_new = CreateView.as_view(model=Comment, fields='__all__',success_url=reverse_lazy('post_detail'))
