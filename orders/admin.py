from django.contrib import admin

from orders.models import Pizza, Sub, Dinner, SubExtra, Topping, Salad, Pasta, IndividualCartItem, IndividualOrderItem

# Register your models here.


# Menu
admin.site.register(Pizza)
admin.site.register(Sub)
admin.site.register(Dinner)
admin.site.register(SubExtra)
admin.site.register(Topping)
admin.site.register(Pasta)
admin.site.register(Salad)

#cart related
admin.site.register(IndividualCartItem)


# order related.
admin.site.register(IndividualOrderItem)
