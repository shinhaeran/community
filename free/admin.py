from django.contrib import admin
from .models import FreePost,FreeComment

# Register your models here.
admin.site.register(FreePost)
admin.site.register(FreeComment)