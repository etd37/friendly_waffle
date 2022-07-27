# Generated by Django 4.0.6 on 2022-07-18 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_remove_city_slug_remove_language_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.language')),
            ],
        ),
    ]
