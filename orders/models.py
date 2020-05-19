from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.






#-----------------------------------------------------------------------
# Base Item
class BaseItem(models.Model):
    """Base class for items. This will contain the item basic properties."""

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64,default="")
    SMALL = 'Small'
    LARGE = 'Large'
    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (LARGE, 'Large')
    )
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,blank=True, default=0) # Blankable for Toppings

    class Meta:
            abstract = True


    def __str__(self):
        if  ( {self.price} > 0 ) :
            return f"{self.name} @ {self.price}"
        else:
            return f"{self.name}"





#-----------------------------------------------------------------------
#
class BaseItemWithPrice(BaseItem):
    """Base class for items which requires a price compulsory"""

    # here i am overriding the base class instance to make it that it cannot be left blank and it should have some price.
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
            abstract = True





#-----------------------------------------------------------------------
#
class BaseItemWithPriceNSize(BaseItemWithPrice):
    """Base class for items which requires a size compulsory"""

    # here i am overriding the base class instance to make it that it cannot be left blank and it should have some size.
    size = models.CharField(max_length=8, choices= BaseItem.SIZE_CHOICES, blank=False)

    class Meta:
            abstract = True

    def __str__(self):
        return f"{self.name} ({self.size}) @ {self.price}"




#-----------------------------------------------------------------------
#
class Pizza(BaseItemWithPriceNSize):
    """ Defines a pizza. Pizza can have 2 types of bases."""

    REGULAR = 'Regular'
    SICILIAN = 'Sicilian'
    CRUST_CHOICES = (
        (REGULAR, 'Regular'),
        (SICILIAN, 'Sicilian')
    )

    crust = models.CharField(max_length=8, choices=CRUST_CHOICES)
    max_toppings = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.crust} Pizza with {self.name} ({self.size}) @ {self.price}"




#-----------------------------------------------------------------------
#
class Dinner(BaseItemWithPriceNSize):
    """ Defines a Dinner here."""

    class Meta:
        verbose_name = "Dinner Platter"
        verbose_name_plural = "Dinner Platters"




#-----------------------------------------------------------------------
#
class Sub(BaseItemWithPriceNSize):
    """ Defines a sub here."""
    pass




#-----------------------------------------------------------------------
#
class SubExtra(BaseItemWithPriceNSize):
    """Define extra-options."""

    def __str__(self):
        return f"{self.name}"





#-----------------------------------------------------------------------
#
class Topping(BaseItem):
    """Define toppings."""

    def __str__(self):
        return f"{self.name}"





#-----------------------------------------------------------------------
#
class Pasta(BaseItemWithPrice):
    """Define pastas."""
    pass





#-----------------------------------------------------------------------
#
class Salad(BaseItemWithPrice):
    """Define salads."""
    pass










