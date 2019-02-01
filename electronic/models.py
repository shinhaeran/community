from django.db import models

# Create your models here.
class ElectronicPost(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.title
