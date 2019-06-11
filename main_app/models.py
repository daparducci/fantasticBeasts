from django.db import models
from django.urls import reverse

# Create your models here.
class Beast(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    magic_abilities = models.TextField(max_length=250)
    dangers = models.TextField(max_length=250)
    habitat = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'beast_id': self.id})