from django.db import models
from django.urls import reverse

RIBBONS = (
    ('G', 'Golden Ribbon'),
    ('R', 'Red Ribbon'),
    ('B', 'Blue Ribbon')
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()
    
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

