# Generated by Django 3.2 on 2024-01-29 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
