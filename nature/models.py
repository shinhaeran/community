from django.db import models
from django.utils import timezone
from account.models import CustomUser
# Create your models here.
class NaturePost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="nature_posts", default=None)
    title = models.CharField(max_length=20)
    content = models.TextField()
    notice = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class NatureComment(models.Model):
    post = models.ForeignKey('NaturePost', on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=20, default=None)
    text = models.TextField()
    depth = models.IntegerField(default=0)
    parent = models.IntegerField(null=True)