# Generated by Django 4.0.6 on 2022-07-15 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_title',
            new_name='title',
        ),
    ]