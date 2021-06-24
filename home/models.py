from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    comment = models.TextField()
 