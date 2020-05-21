from django.contrib import admin

from orders.models import Pizza, Sub, Dinner, SubExtra, Topping, Salad, Pasta, IndividualCartItem, IndividualOrderItem, OrderDetail

# Register your models here.

class OrderDetailAdmin(admin.ModelAdmin):
    ''' order detal admin pane customization '''
    list_display = ('ordertime', 'user', 'contact', 'orderprice', 'status')
    list_filter = ['ordertime', 'status']



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
admin.site.register(OrderDetail, OrderDetailAdmin)
