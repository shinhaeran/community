# Generated by Django 2.1.5 on 2019-02-09 16:22

from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_summernote', '0002_update-help_text'),
        ('agriculture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummerNote',
            fields=[
                ('attachment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_summernote.Attachment')),
                ('summer_field', django_summernote.fields.SummernoteTextField(default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('django_summernote.attachment',),
        ),
    ]
