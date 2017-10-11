from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[{}]의 댓글 [{}]"'.format(self.post, self.message)
