# Generated by Django 4.0.3 on 2022-04-10 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0005_alter_rating_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='author',
            new_name='user',
        ),
    ]
