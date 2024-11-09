from django.db import models

# Create your models here.
class Artical(models.Model):
    name=models.CharField(max_length=60)
    content=models.TextField()
    created=models.DateField(auto_now_add=True)
class Characters(models.Model):
    first_name=models.CharField(max_length=60)
    second_name=models.CharField(max_length=60)
    image=models.ImageField()
    discription=models.TextField()
class Technique(models.Model):
    red_name=models.CharField(max_length=60)
    damage_amount=models.IntegerField()
    owner=models.ForeignKey(Characters,models.CASCADE)
