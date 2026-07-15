from django.db import models

# Create your models here.
class BookModel(models.Model):
    mualif = models.CharField(max_length=500)
    name = models.CharField(max_length=225,unique=True)
    info = models.TextField()
    
    def __str__(self):
        return self.username
    