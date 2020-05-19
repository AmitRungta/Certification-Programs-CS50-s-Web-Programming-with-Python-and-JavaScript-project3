from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# Base Item
class BaseItem(models.Model):
    """Base class for items. This will contain the item basic properties."""

    name = models.CharField(max_length=64)
    SMALL = 'Small'
    LARGE = 'Large'
    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (LARGE, 'Large')
    )
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, blank=True)
    price = models.IntegerField(blank=True, default=0) # Blankable for Toppings

    class Meta:
            abstract = True


    def __str__(self):
        return f"{self.name} _ {self.price}"

    def is_valid_item(self):
        return (self.price >= 0)



class Pizza(BaseItem):
    """ Defines a pizza. Pizza can have 2 types of bases."""

    CRUST_CHOICES = (
        ('REGULAR', 'Regular'),
        ('SICILIAN', 'Sicilian')
    )

    # here i am overriding the base class instance to make it that it cannot be left blank and it should have some size.
    size = models.CharField(max_length=8, choices= BaseItem.SIZE_CHOICES, blank=False)

    crust = models.CharField(max_length=8, choices=CRUST_CHOICES)
    max_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.crust} Pizza with {self.name} ({self.size}) _ {self.price}"




