# Generated by Django 3.2 on 2024-01-29 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='movies',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.movie'),
        ),
    ]