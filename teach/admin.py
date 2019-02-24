from django.contrib import admin
from .models import TeachPost,TeachComment

# Register your models here.
admin.site.register(TeachPost)
admin.site.register(TeachComment)