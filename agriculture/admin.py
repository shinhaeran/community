from django.contrib import admin
from .models import AgriculturePost, AgricultureComment

# Register your models here.

admin.site.register(AgriculturePost)
admin.site.register(AgricultureComment)