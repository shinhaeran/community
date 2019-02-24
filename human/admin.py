from django.contrib import admin
from .models import HumanPost,HumanComment

# Register your models here.
admin.site.register(HumanPost)
admin.site.register(HumanComment)