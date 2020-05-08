from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
import misaka
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=500, default='')
    created_at = models.DateTimeField(default=timezone.now)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs= {'pk':self.pk})

    def save(self, *args, **kwargs):
        self.message_html= misaka.html(self.message)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together= ['user','title']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_list')






























