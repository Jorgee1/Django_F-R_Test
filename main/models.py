from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Languaje(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Person(models.Model):
    MALE   = 'M'
    FEMALE = 'F'
    gender_choice = ((MALE, 'Male'),(FEMALE, 'Female'))


    person_id     = models.CharField(max_length=10 , default="", unique=True)
    first_name    = models.CharField(max_length=20 , default="")
    last_name     = models.CharField(max_length=20 , default="")
    email         = models.CharField(max_length=200, default="", unique=True)
    gender        = models.CharField(max_length=2  , choices=gender_choice, default=None, null=True)
    city          = models.ForeignKey(City,  on_delete=models.CASCADE, default=None, null=True)
    color         = models.ForeignKey(Color, on_delete=models.CASCADE, default=None, null=True)
    languaje      = models.ForeignKey(Languaje, on_delete=models.CASCADE, default=None, null=True)
    favorite_food = models.CharField(max_length=400, default="")


    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ('first_name',)
