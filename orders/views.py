''' This view is used for showing the different view options '''
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Pizza, Sub, Dinner, SubExtra, Topping, Salad, Pasta, BaseItem


#---------------------------------------------------------------------------
#
def get_menu_items(productlist):
    ''' this function creates a menu items for the product list as per its serving size.'''

    # generate list of unique item names.
    names = []
    for product in productlist:
        if product.name not in names:
            names.append(product.name)

    # Parse different sizes with corresponding product name
    items = []
    for name in names:
        item = {}
        item["name"] = name
        for product in productlist:
            try:
                if product.name == name and product.size == BaseItem.SMALL:
                    item['id_small'] = product.id
                    item['price_small'] = product.price
                elif product.name == name and product.size == BaseItem.LARGE:
                    item['id_large'] = product.id
                    item['price_large'] = product.price
            # if product has no size attribute (AttributeError)
            except:
                item['id'] = product.id
                item['price'] = product.price
        items.append(item)

    return items





# Create your views here.
# @login_required(login_url="/accounts/login/")
def index(request):
    ''' default page to show the menu '''
    context = {
        "regular_pizzas": get_menu_items(Pizza.objects.filter(crust=Pizza.REGULAR).all()),
        "sicilian_pizzas": get_menu_items(Pizza.objects.filter(crust=Pizza.SICILIAN).all()),
        "toppings": Topping.objects.all(),
        "subs": get_menu_items(Sub.objects.all()),
        "extras": get_menu_items(SubExtra.objects.all()),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "dinners": get_menu_items(Dinner.objects.all())
        }
    return render(request, 'orders/menu.html', context)



@login_required(login_url='accounts:login')
def add_item(request, item_id):
    ''' Function to ask for adding a new item into cart.
    This will get post message from the form with updated data '''

    if request.method == 'GET':
        try:
            baseitem = BaseItem.objects.get(pk=item_id)
        except:
            return HttpResponseRedirect(reverse('menu'))

        context = {
            "item": baseitem,
        }

        # check if this is for pizza and it requires custom toppings
        if hasattr(baseitem, 'pizza') and baseitem.pizza.max_toppings > 0:
            context['toppings'] = Topping.objects.all()
            context['max_toppings'] = baseitem.pizza.max_toppings
        # check if this is for sub and can have extras
        elif hasattr(baseitem, 'sub'):
            context['extras'] = SubExtra.objects.filter(size=baseitem.size).all()

        return render(request, 'orders/add_item.html', context)

    # AmitTempCode Handle the post case...








@login_required(login_url='accounts:login')
def manage_admin_order(request):
    ''' Function to manage orders by super user... '''

    if not request.user.is_superuser:
        return HttpResponseForbidden()

    # AmitTempCode
    context = {}
    return render(request, 'orders/menu.html', context)
