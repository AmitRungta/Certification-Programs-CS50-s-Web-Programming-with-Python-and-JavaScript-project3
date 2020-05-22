''' This view is used for showing the different view options '''
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Pizza, Sub, Dinner, SubExtra, Topping, Salad, Pasta, BaseItem, IndividualCartItem, IndividualOrderItem, OrderDetail


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


def get_total_items_in_cart_count(request):
    ''' function to get total items in the cart '''
    if not request.user.is_authenticated:
        return 0
    cartitemscount = IndividualCartItem.objects.filter(user=request.user).count()
    return cartitemscount



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
    # now set the item count in hte cart.
    context['item_in_cart_count'] = get_total_items_in_cart_count(request)
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

        # now set the item count in hte cart.
        context['item_in_cart_count'] = get_total_items_in_cart_count(request)
        return render(request, 'orders/add_item.html', context)

    # we are here this means we have received a post message command.
    # Hence lets add this item to our cart.
    try:
        baseitem = BaseItem.objects.get(pk=item_id)
    except:
        return HttpResponseNotFound()

    # lets get the basic data from the form.
    selquantity = int(request.POST['quantity'])
    totalprice = float(request.POST['total-price'])
    extrasubcount = int(request.POST.get('extra-sub-count', 0))
    add_to_cart_and_checkout = request.POST.get('add-to-cart-checkout', False)



    try:
        cart_item = IndividualCartItem.objects.create(user=request.user, baseitem=baseitem, quantity=selquantity)

        # Now check if we have toppings then try and set each topping data.
        max_toppings = 0
        if hasattr(baseitem, 'pizza') and baseitem.pizza.max_toppings > 0:
            max_toppings = baseitem.pizza.max_toppings

        for loopindex in range(max_toppings):
            toppingid = request.POST.get(f'topping-{loopindex+1}', False)
            if toppingid:
                toppingdata = Topping.objects.get(pk=toppingid)
                cart_item.toppings.add(toppingdata)

        for loopindex in range(extrasubcount):
            extraid = request.POST.get(f'extra-{loopindex+1}', False)
            if extraid:
                extradata = SubExtra.objects.get(pk=extraid)
                cart_item.subextra.add(extradata)

        cart_item.price = totalprice
        cart_item.save()

    except:
        cart_item.delete()
        return HttpResponseNotFound()

    if add_to_cart_and_checkout:
        return HttpResponseRedirect(reverse('orders:cart'))
    else:
        return HttpResponseRedirect(reverse('orders:menu'))



@login_required(login_url='accounts:login')
def cart_item_list(request):
    ''' Function to display the current cart items... '''
    cartitems = IndividualCartItem.objects.filter(user=request.user).all()

    context = {
        "cartitems": cartitems
    }

    # lets get the cart total.
    cart_total_cost = 0
    for item in cartitems:
        cart_total_cost += item.price

    context['cart_total_cost'] = cart_total_cost

    # now set the item count in hte cart.
    context['item_in_cart_count'] = get_total_items_in_cart_count(request)
    return render(request, 'orders/cartitemlist.html', context)



@login_required(login_url='accounts:login')
def delete_cart_item(request, cartitem_id):
    ''' Function to delete an item from the cart... '''

    if request.method == 'GET':
        return HttpResponseNotFound()

    try:
        cartitem = IndividualCartItem.objects.get(pk=cartitem_id)
        cartitem.delete()
    except IndividualCartItem.DoesNotExist:
        return HttpResponseNotFound()

    return HttpResponseRedirect(reverse('orders:cart'))





@login_required(login_url='accounts:login')
def confirm_order(request):
    ''' Function to place a new order from our current cart ... '''

    if request.method == 'GET':
        return HttpResponseNotFound()

    # first of all get the complete cart items.
    cartitems = IndividualCartItem.objects.filter(user=request.user).all()
    context = {
        "cartitems": cartitems
    }

    # lets get the cart total.
    cart_total_cost = 0
    for item in cartitems:
        cart_total_cost += item.price
    context['cart_total_cost'] = cart_total_cost

    # get the details from the form.
    context['contact'] = request.POST['contact']
    context['address'] = request.POST['address']
    context['message'] = request.POST['message']
    context['for_confimation_readonly'] = 'True'

    # do not set the cart item count here as in this case i donot want to show any item in cart.
    # context['item_in_cart_count'] = get_total_items_in_cart_count(request)
    return render(request, 'orders/cartitemlist.html', context)





@login_required(login_url='accounts:login')
def place_order(request):
    ''' Function to place a new order from our current cart ... '''

    if request.method == 'GET':
        return HttpResponseNotFound()

    # first of all get the complete cart items.
    cartitems = IndividualCartItem.objects.filter(user=request.user).all()

    # lets get the cart total.
    cart_total_cost = 0
    for item in cartitems:
        cart_total_cost += item.price

    # get the details from the form.
    contact = request.POST['contact']
    address = request.POST['address']
    message = request.POST['message']

    # now lets create the order..
    orderdetail = OrderDetail.objects.create(
        user=request.user,
        orderprice=cart_total_cost,
        contact=contact,
        address=address,
        message=message,
    )

    # now lets add each item of this cart in the order
    for item in cartitems:
        orderitem = IndividualOrderItem.objects.create(
            user=request.user,
            baseitem=item.baseitem,
            quantity=item.quantity,
            price=item.price
            )

        # now lets add each topping from the cart to this order
        for topping in item.toppings.all():
            orderitem.toppings.add(topping)

        # now lets add each extra from the cart to this order
        for extra in item.subextra.all():
            orderitem.subextra.add(extra)

        # we have completed the order item hence lets add this in our order
        orderdetail.orderitems.add(orderitem)

    # as we have completed our order hence lets delete this cart item.
    cartitems.delete()
    orderdetail.save()

    return HttpResponseRedirect(reverse('orders:order_history'))





@login_required(login_url='accounts:login')
def order_history(request):
    ''' Function to get the order history for this customer ... '''

    if request.method == 'POST':
        return HttpResponseNotFound()

    context = {
        "orders_list": OrderDetail.objects.filter(user=request.user).order_by('-ordertime')
    }

    # now set the item count in hte cart.
    context['item_in_cart_count'] = get_total_items_in_cart_count(request)
    return render(request, 'orders/order_history.html', context)




@login_required(login_url='accounts:login')
def order_detail(request, order_id):
    ''' Function to get the details of this order. Here we will validate that the order should belong to this customer... '''

    try:
        if request.user.is_superuser:
            orderdetail = OrderDetail.objects.get(pk=order_id)
        else:
            orderdetail = OrderDetail.objects.get(pk=order_id, user=request.user)
    except OrderDetail.DoesNotExist:
        return HttpResponseNotFound()

    context = {
        "orderdetail": orderdetail
    }

    # now set the item count in hte cart.
    context['item_in_cart_count'] = get_total_items_in_cart_count(request)
    return render(request, 'orders/order_detail.html', context)




@login_required(login_url='accounts:login')
def manage_admin_order(request):
    ''' Function to manage orders by super user... '''

    if not request.user.is_superuser:
        return HttpResponseForbidden()

    # if this is a post message then its for updating the status of any order.
    if request.method == 'POST':
        try:
            orderid = request.POST['orderid']
            status = request.POST['status']
            orderdetail = OrderDetail.objects.get(pk=orderid)
            #update the status
            if status == "Cancel":
                # we want to cancel this order hence elete it.
                # now lets delete each individual item row for this order
                for item in orderdetail.orderitems.all():
                    item.delete()

                # now lets delete this order completely
                orderdetail.delete()
            elif orderdetail.status != status:
                orderdetail.status = status
                orderdetail.save()

            return HttpResponseRedirect(reverse('orders:manage_admin_order'))
        except:
            return HttpResponseNotFound()


    context = {
        "ordered_orders": OrderDetail.objects.filter(status=OrderDetail.ORDERED).order_by('-ordertime'),
        "preparing_orders": OrderDetail.objects.filter(status=OrderDetail.PREPARING).order_by('-ordertime'),
        "shipped_orders": OrderDetail.objects.filter(status=OrderDetail.SHIPPED).order_by('-ordertime'),
        "delivered_orders": OrderDetail.objects.filter(status=OrderDetail.DELIVERED).order_by('-ordertime')
    }

    return render(request, 'orders/manage_admin_order.html', context)
