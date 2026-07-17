from django.db import models

# Create your models here.



class BookModel(models.Model):
    mualif = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    info = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to="books/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name