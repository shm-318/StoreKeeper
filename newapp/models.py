from django.db import models

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

