from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Stade(models.Model):
    name=models.CharField(max_length=200)
    nb_tickets=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name
    def update(self):
        self.nb_tickets = self.nb_tickets - 1
        return self.nb_tickets


class Classe(models.Model):
    name = models.CharField(max_length=1)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name




class Payment(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Coor(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    dof=models.DateTimeField(auto_now_add=True)
    #classA=models.BooleanField(null=False)
    #classB=models.BooleanField(null=False)
    #visa=models.BooleanField(null=False)
    #pay=models.BooleanField(null=False)
    #dah=models.BooleanField(null=False)
    #mas=models.BooleanField(null=False)
    #code=models.PositiveIntegerField()
    def __str__(self):
        return self.name


class Room(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    Session=models.CharField(max_length=30,default=None)
    stade=models.ForeignKey(Stade,on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
