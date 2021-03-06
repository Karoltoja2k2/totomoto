from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Offer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offer', null=True)

    title = models.CharField(max_length=200, null=True)

    dsc = models.CharField(max_length=3000, null=True)


    category = models.CharField(max_length=30, null=True)
    marka = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=20, null=True)
    stan = models.CharField(max_length=30, null=True)
    prod_year = models.IntegerField(null=True)
    mileage = models.IntegerField(null=True)
    cap = models.IntegerField(null=True)
    fuel = models.CharField(max_length=20, null=True)
    power = models.IntegerField(null=True)
    naped = models.CharField(max_length=30, null=True)
    gear_box = models.CharField(max_length=20, null=True)
    colour = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)


    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title

    def get_first_image(self):
        return self.images_set.first()

class Images(models.Model):
    offer = models.ForeignKey(Offer, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images')


class Userinf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userinf', null=True)
    phone_num = models.IntegerField(null=True)
    adress = models.CharField(max_length=50, null=True)


#samochody


class CarMark(models.Model):
    marka = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.marka

class Category(models.Model):
    category = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.category

class Stan(models.Model):
    stan = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.stan


class Status(models.Model):
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.status


class Type(models.Model):
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.type


class Fuel(models.Model):
    fuel = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.fuel

class GearBox(models.Model):
    gear_box = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.gear_box

class Naped(models.Model):
    naped = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.naped




