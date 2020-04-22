from django.db import models

# Create your models here.
class courses(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    