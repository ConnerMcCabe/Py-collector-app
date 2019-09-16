from django.db import models
from django.urls import reverse

# Create your models here.

class Rat(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'rat_id': self.id})

