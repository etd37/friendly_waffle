from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='City name')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name= 'City Name'
        verbose_name_plural = "Names"

    def __str__(self):
        return self.name
