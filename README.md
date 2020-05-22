# Project 3

Web Programming with Python and JavaScript

## Introductions

In this project i have tried to create a order website for Pinnochio’s Pizza & Subs. In this website user can come and see the menu and customize them as per their needs. To order something from the site user needs to be registered with the site. If the user is already a registered member then he can login to the site and can place order. Here user can also see his previous orders and their current state. 

## Database 

While creating the database i have divided all the content into 4 major components.
*  **BaseItem** : this is the base table from which each menu item table is derived. This table mainly consist of item name, Description , portion size , and individual price. Each menu component like Pizza / Sub / Dinner / Pasta / Salad / extra on the sub / pizza toppings. Some items which required additional options contain them in their individual classs like pizza contains base type ( regular / Sicilian ) and additiona ltopping.
* **IndividualCartItem** : this table contains the items in the cart as per the individual user. Individual item consist of BaseItem, its quantity and desired toppings(for pizza)/ extra ( for sub). It also contains the cost for this item with addons and quantity.
* **IndividualOrderItem** : this is similar to the cart item. It just differs that this is used for the final order when placed by the user.
* **OrderDetail** : This is the final order data. It consist of IndividualOrderItem and the user details ( like contatc and address). This also contains the current status of the order ( Ordered / Preparing / On Way / Delivered). Once the order is received this can be seen by the administrator / any user in superuser group can update the status of the order. The order status moves from one state to the next one. User can also see his orders status in the order history option.


## Requirements :

* **Menu** : The main page of the site shows the menu in a tabular form. There is a top sticky nav bar which is used for quick reference to any menu item group. In the menu we have shown the items as per size ( if applicable ) and any item can be added to the cart for ordering by the link next to the item.  

* **Adding Items** : All the menu itms have been categorised into tables as per their properties. These items can be added from the admin UI. Also we have created a add_default_items.py cile which contains the functions to add all the items in the clean database to match the standard menu.

* **Registration, Login, Logout** : To manage the user authorisation i have used the django inbuilt authorisation model. In the default signup it just shows the username and password options and hence to show the firstname / last name / email address i have extended the UserCreationForm to allow the additional fields.

* **Shopping Cart** : Once a user is logged in any item that the user selects is added into the database with that user (IndividualCartItem). Hence even if the user logsout and login again from a different computer he gets the same cart items already added. When the user selects a item from the menu they are asked to customize the item by selecting its desired quantity and toppings/ extras if supported. While customizing user is also able to see the current cost of the item with customization. Once customization is completed user can add the item to the cart and then continue with adding new items or checkout the cart. When items are added to the cart a small tip above the cart link shows the current items count in the cart. In the cart user has a option to delete the items from the cart itself.  

* **Placing an Order** : For the logged user, they can place order for the items in their cart. While placing the order for the items in the cart user is also required to specify their contact number and address for delivery. In case if user has some specific request he can also specify it in the optional message box for the chef ( like : make pizza to be extra cripsy...). Once the user selects checkout for the cart he is shown his current selection for verifcation with the total bill amount. In here user has a option to either modify his order or confirm and place the order.    

* **Viewing Orders** : Every logged in customer has a option to check for the previous orders he has placed. This shows the list of the previous orders placed by the user and user can select any order from here to get the order details.


* **Personal Touch** : When the current logged in user is having the administrative privileges then he is shown with an additional option of managing the orders. In here administrator can update the status of the pending orders whcih are reflected to the users order state or can cancel any order if required. This page shows all the orders in the various states ( Ordered / Preparing / On Way / Delivered) groupped as per the state, ordered as per order time and he can chage the order state from here. Orders which have reached the state of Delivered does not allow to change the state. IN this list also administrator can check the details of any order by clicking on the order ID.



