from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User,null= True, on_delete=models.CASCADE)
    bio = models.TextField()
    def createPainting(self,name,price,size,image=""):
        painting= Paintings()
        painting.Author= self
        painting.name=name
        painting.image=image
        painting.price=price
        painting.size=size
        painting.save()
    def __str__(self):
        return self.user.first_name    
class Paintings(models.Model):
    name = models.TextField()
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    price = models.IntegerField()
    size= models.CharField(max_length=64)
    image = models.ImageField((""), upload_to='./static/imgs/paintings', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name
# Author class
