# Generated by Django 4.0.6 on 2022-07-18 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_language_alter_city_options_alter_city_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City Name', 'verbose_name_plural': 'City Names'},
        ),
    ]
