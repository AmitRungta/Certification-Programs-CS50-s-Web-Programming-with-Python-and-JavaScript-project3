''' Create your models here. '''

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




#-----------------------------------------------------------------------
# Base Item
class BaseItem(models.Model):
    """Base class for items. This will contain the item basic properties."""

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64, blank=True)
    SMALL = 'Small'
    LARGE = 'Large'
    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (LARGE, 'Large')
    )
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, blank=True)
     # Blankable for Toppings
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)

    def __str__(self):
        retstr = f"{self.name}"
        if self.is_size_required():
            retstr += f" ({self.size})"

        if self.is_price_required():
            retstr += f" @{self.price})"
        return retstr



    def is_price_required(self):
        ''' check if price is required '''
        return False

    def is_size_required(self):
        ''' check if size is required '''
        return False


    def is_valid_item(self):
        ''' check if is valid item for saving '''
        if self.is_price_required():
            if self.price <= 0:
                return "Price is not valid"

        if self.is_size_required():
            if self.size == "":
                return "Portion size is not specified"

        return ""

    def save(self, *args, **kwargs):
        # Check if we can save with the current settings or not.
        errmsg = self.is_valid_item()
        if len(errmsg) > 0:
            raise ValueError(errmsg)
        super().save(*args, **kwargs)


#-----------------------------------------------------------------------
#
class Pizza(BaseItem):
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


    def is_price_required(self):
        return True

    def is_size_required(self):
        return True




#-----------------------------------------------------------------------
#
class Dinner(BaseItem):
    """ Defines a Dinner here."""

    class Meta:
        verbose_name = "Dinner Platter"
        verbose_name_plural = "Dinner Platters"

    def is_price_required(self):
        return True

    def is_size_required(self):
        return True



#-----------------------------------------------------------------------
#
class Sub(BaseItem):
    """ Defines a sub here."""

    def is_price_required(self):
        return True

    def is_size_required(self):
        return True




#-----------------------------------------------------------------------
#
class SubExtra(BaseItem):
    """Define extra-options."""

    def __str__(self):
        return f"{self.name}"

    def is_price_required(self):
        return True

    def is_size_required(self):
        return True




#-----------------------------------------------------------------------
#
class Topping(BaseItem):
    """Define toppings."""




#-----------------------------------------------------------------------
#
class Pasta(BaseItem):
    """Define pastas."""

    def is_price_required(self):
        return True

    def is_size_required(self):
        return False





#-----------------------------------------------------------------------
#
class Salad(BaseItem):
    """Define salads."""

    def is_price_required(self):
        return True

    def is_size_required(self):
        return False





#-----------------------------------------------------------------------
#
class IndividualCartItem(models.Model):
    """Individual Cart items"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    baseitem = models.ForeignKey(BaseItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # For pizza
    toppings = models.ManyToManyField(Topping, blank=True, related_name='carts_toppings')
    # For Sub
    subextra = models.ManyToManyField(SubExtra, blank=True, related_name='carts_extras')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user} {self.baseitem} {self.quantity} "





#-----------------------------------------------------------------------
#
class IndividualOrderItem(models.Model):
    """Individual Order items"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_item')
    baseitem = models.ForeignKey(BaseItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # For pizza
    toppings = models.ManyToManyField(Topping, blank=True, related_name='orders_toppings')
    # For Sub
    subextra = models.ManyToManyField(SubExtra, blank=True, related_name='orders_extras')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user} {self.baseitem} {self.quantity} "




#-----------------------------------------------------------------------
#
class OrderDetail(models.Model):
    """ Collection of all the order items from the cart."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    # as every order item is just associated with one order hence they are in onetomany relationship
    # with order but as OneToManyField is not avialable in Django ORM hence either i can use Foreign
    # Key in IndividualOrderItem or can use ManyToMany. As using ManyToMany wont effect us anyhow
    # hence we will use this and not Foreign Key.
    orderitems = models.ManyToManyField(IndividualOrderItem, related_name='order')
    orderprice = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    ordertime = models.DateTimeField(default=timezone.now)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    message = models.CharField(max_length=100, blank=True)
    ORDERED = 'Ordered'
    PREPARING = 'Preparing'
    SHIPPED = 'On Way'
    DELIVERED = 'Delivered'
    STATUS_CHOCIES = (
        (ORDERED, 'Ordered'),
        (PREPARING, 'Preparing'),
        (SHIPPED, 'On Way'),
        (DELIVERED, 'Delivered')
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOCIES, default=ORDERED)

    def __str__(self):
        return f"{self.user} {self.contact} {self.ordertime} @ {self.status}"
