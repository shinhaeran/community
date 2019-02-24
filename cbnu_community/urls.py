"""cbnu_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('account.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('agriculture/', include('agriculture.urls')),
    path('business/', include('business.urls')),
    path('electronic/', include('electronic.urls')),
    path('engineer/', include('engineer.urls')),
    path('free/', include('free.urls')),
    path('human/', include('human.urls')),
    path('life/', include('life.urls')),
    path('nature/', include('nature.urls')),
    path('social/', include('social.urls')),
    path('teach/', include('teach.urls')),
    path('summernote/', include('django_summernote.urls')),
    url(r'^notifications/', include('notify.urls', 'notifications')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)