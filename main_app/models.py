from django.db import models
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class RatCreate(CreateView):
    model = Rat
    fields = '__all__'
    success_url = '/rats/'
class RatUpdate(UpdateView):
    model = Rat
    fields = ['breed', 'description', 'age']
class RatDelete(DeleteView):
    model = Rat
    success_url = '/rats/'