from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee (models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    firstName = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    email = models.EmailField(max_length=200)
    phoneNumber = PhoneNumberField(blank=True)
    address = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    position = models.TextField(max_length=100)
    background = models.CharField(max_length=500)