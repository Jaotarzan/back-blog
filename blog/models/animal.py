from django.db import models

class Animal(models.Model):
    species = models.CharField(max_length=150)  
    foto = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.species