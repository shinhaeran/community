from django.contrib import admin
from .models import ElectronicPost,ElectronicComment

# Register your models here.

admin.site.register(ElectronicPost)
admin.site.register(ElectronicComment)