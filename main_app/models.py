from django.db import models
from django.urls import reverse
from datetime import date

RIBBONS = (
    ('G', 'Golden Ribbon'),
    ('R', 'Red Ribbon'),
    ('B', 'Blue Ribbon')
)

class Nest(models.Model):
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.location} in {self.city}'

    def get_absolute_url(self):
        return reverse('finch_detail', kwargs={'pk': self.id})

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()
    nests = models.ManyToManyField(Nest)

    def has_ribbon(self):
        return self.ribbon_set.all > 0
    
    def __str__ (self):
        return (f'{self.name}, a {self.color} finch, {self.age} years old')
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"finch_id": self.id})
    
class Ribbon(models.Model):
    date = models.DateField('Day of Gift')
    color = models.CharField(
        max_length=1,
        choices=RIBBONS,
        default=[0][0]  
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_color_display()}, gifted on {self.date}'

class Meta:
    ordering = ['-date']