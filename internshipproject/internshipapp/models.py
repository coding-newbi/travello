from django.db import models

# Create your models here.
class travel(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='piks')
    desc=models.TextField()
class team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()



    def __str__(self):
        return self.name

