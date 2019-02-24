from django.contrib import admin
from .models import SocialPost,SocialComment

# Register your models here.
admin.site.register(SocialPost)
admin.site.register(SocialComment)
