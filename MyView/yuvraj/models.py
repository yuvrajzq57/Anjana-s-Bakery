from email.headerregistry import Address
from django.db import models


# Create your models here.
class About(models.Model):
    Name = models.CharField(default='', max_length=123)
    Address = models.CharField(default='', max_length=123)
    Landmark = models.CharField(default='', max_length=123)
    City = models.CharField(default='', max_length=123)
    State = models.CharField(default='', max_length=123)
    Zip = models.CharField(default='', max_length=123)
    header_image = models.ImageField(null = True ,  blank=True)

    def __str__(self):
        return f"{self.Name} - {self.City}"
