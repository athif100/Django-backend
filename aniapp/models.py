from django.db import models

# Create your models here.
class Artical(models.Model):
    name=models.CharField(max_length=60)
    content=models.TextField()
    created=models.DateField(auto_now_add=True)