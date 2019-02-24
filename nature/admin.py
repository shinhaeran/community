from django.contrib import admin
from .models import NaturePost,NatureComment

# Register your models here.
admin.site.register(NaturePost)
admin.site.register(NatureComment)