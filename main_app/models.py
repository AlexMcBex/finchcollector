from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__ (self):
        return (f'{self.name}, a {self.color} finch, {self.age} years old')
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})
    