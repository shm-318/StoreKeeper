from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    item=models.CharField(max_length=200)
    quantity=models.CharField(max_length=200)
    date_ordered= models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.item

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE) #on delete argument required since djnago 2.x

    #extra attributes

    StoreName = models.CharField(max_length=300)

    profile_pic =models.ImageField(upload_to='profile_pic',blank=True) #if the user uploads any profile pic, it gets saved to this section.

    def __str__(self):
        return self.user.username
