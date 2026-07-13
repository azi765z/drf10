from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=500)
    email = models.EmailField(unique=True,max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    