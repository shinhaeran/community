# Generated by Django 2.1.5 on 2019-02-24 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teach', '0002_auto_20190224_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachpost',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='teach_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
