# Generated by Django 4.1.1 on 2022-09-16 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_author_username_alter_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='id',
            new_name='user',
        ),
    ]
