from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='City name',
                            unique=True)

    class Meta:
        verbose_name = 'City Name'
        verbose_name_plural = "City Names"

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Programming Language',
                            unique=True)

    class Meta:
        verbose_name = 'Programming Language'
        verbose_name_plural = 'Programming Languages'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    description = models.TextField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)     #automatically adds date when enters DB

    def __str__(self):
        return self.title
