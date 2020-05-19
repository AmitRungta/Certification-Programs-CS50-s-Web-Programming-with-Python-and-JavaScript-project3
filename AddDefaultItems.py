# in this file we will add the desfualt items in our database.
from orders.models import Pizza , Sub , Dinner , SubExtra , Topping , Salad , Pasta , BaseItem


def addPizza():
    pizza = Pizza(name="Cheese" , size=BaseItem.SMALL , price=12.70 , crust=Pizza.REGULAR , max_toppings=0)
    pizza.save()

    pizza = Pizza(name="Cheese" , size=BaseItem.LARGE , price=17.95 , crust=Pizza.REGULAR , max_toppings=0)
    pizza.save()

    pizza = Pizza(name="1 topping" , size=BaseItem.SMALL , price=13.70 , crust=Pizza.REGULAR , max_toppings=1)
    pizza.save()

    pizza = Pizza(name="1 topping" , size=BaseItem.LARGE , price=19.95 , crust=Pizza.REGULAR , max_toppings=1)
    pizza.save()

    pizza = Pizza(name="2 topping" , size=BaseItem.SMALL , price=15.20 , crust=Pizza.REGULAR , max_toppings=2)
    pizza.save()

    pizza = Pizza(name="2 topping" , size=BaseItem.LARGE , price=21.95 , crust=Pizza.REGULAR , max_toppings=2)
    pizza.save()

    pizza = Pizza(name="3 topping" , size=BaseItem.SMALL , price=16.20 , crust=Pizza.REGULAR , max_toppings=3)
    pizza.save()

    pizza = Pizza(name="3 topping" , size=BaseItem.LARGE , price=23.95 , crust=Pizza.REGULAR , max_toppings=3)
    pizza.save()

    pizza = Pizza(name="Special" , size=BaseItem.SMALL , price=17.75 , crust=Pizza.REGULAR , max_toppings=5)
    pizza.save()

    pizza = Pizza(name="Special" , size=BaseItem.LARGE , price=25.95 , crust=Pizza.REGULAR , max_toppings=5)
    pizza.save()



    pizza = Pizza(name="Cheese" , size=BaseItem.SMALL , price=24.45 , crust=Pizza.SICILIAN , max_toppings=0)
    pizza.save()

    pizza = Pizza(name="Cheese" , size=BaseItem.LARGE , price=38.70 , crust=Pizza.SICILIAN , max_toppings=0)
    pizza.save()

    pizza = Pizza(name="1 topping" , size=BaseItem.SMALL , price=26.45 , crust=Pizza.SICILIAN , max_toppings=1)
    pizza.save()

    pizza = Pizza(name="1 topping" , size=BaseItem.LARGE , price=40.70 , crust=Pizza.SICILIAN , max_toppings=1)
    pizza.save()

    pizza = Pizza(name="2 topping" , size=BaseItem.SMALL , price=28.45 , crust=Pizza.SICILIAN , max_toppings=2)
    pizza.save()

    pizza = Pizza(name="2 topping" , size=BaseItem.LARGE , price=42.70 , crust=Pizza.SICILIAN , max_toppings=2)
    pizza.save()

    pizza = Pizza(name="3 topping" , size=BaseItem.SMALL , price=29.45 , crust=Pizza.SICILIAN , max_toppings=3)
    pizza.save()

    pizza = Pizza(name="3 topping" , size=BaseItem.LARGE , price=44.70 , crust=Pizza.SICILIAN , max_toppings=3)
    pizza.save()

    pizza = Pizza(name="Special" , size=BaseItem.SMALL , price=30.45 , crust=Pizza.SICILIAN , max_toppings=5)
    pizza.save()

    pizza = Pizza(name="Special" , size=BaseItem.LARGE , price=45.70 , crust=Pizza.SICILIAN , max_toppings=5)
    pizza.save()



def addToppings():
    toppinglist = ['Pepperoni', \
                    'Sausage', \
                    'Mushrooms', \
                    'Onions', \
                    'Ham', \
                    'Canadian Bacon', \
                    'Pineapple', \
                    'Eggplant', \
                    'Tomato & Basil', \
                    'Green Peppers', \
                    'Hamburger', \
                    'Spinach', \
                    'Artichoke', \
                    'Buffalo Chicken', \
                    'Barbecue Chicken', \
                    'Anchovies', \
                    'Black Olives', \
                    'Fresh Garlic', \
                    'Zucchini',
                    ]
    
    for topping in toppinglist :
        toppingentry = Topping ( name=topping)
        toppingentry.save()
        


def addDinner():
    dinner = Dinner(name="Garden Salad" , size=BaseItem.SMALL , price=40.00 )
    dinner.save()

    dinner = Dinner(name="Garden Salad" , size=BaseItem.LARGE , price=65.00 )
    dinner.save()

    dinner = Dinner(name="Greek Salad" , size=BaseItem.SMALL , price=50.00 )
    dinner.save()

    dinner = Dinner(name="Greek Salad" , size=BaseItem.LARGE , price=75.00 )
    dinner.save()

    dinner = Dinner(name="Antipasto" , size=BaseItem.SMALL , price=50.00 )
    dinner.save()

    dinner = Dinner(name="Antipasto" , size=BaseItem.LARGE , price=75.00 )
    dinner.save()

    dinner = Dinner(name="Baked Ziti" , size=BaseItem.SMALL , price=40.00 )
    dinner.save()

    dinner = Dinner(name="Baked Ziti" , size=BaseItem.LARGE , price=65.00 )
    dinner.save()

    dinner = Dinner(name="Meatball Parm" , size=BaseItem.SMALL , price=50.00 )
    dinner.save()

    dinner = Dinner(name="Meatball Parm" , size=BaseItem.LARGE , price=75.00 )
    dinner.save()

    dinner = Dinner(name="Chicken Parm" , size=BaseItem.SMALL , price=55.00 )
    dinner.save()

    dinner = Dinner(name="Chicken Parm" , size=BaseItem.LARGE , price=85 )
    dinner.save()




def addSub():
    sub = Sub(name="Cheese" , size=BaseItem.SMALL , price=6.50 )
    sub.save()

    sub = Sub(name="Cheese" , size=BaseItem.LARGE , price=7.95 )
    sub.save()

    sub = Sub(name="Italian" , size=BaseItem.SMALL , price=6.50 )
    sub.save()

    sub = Sub(name="Italian" , size=BaseItem.LARGE , price=7.95 )
    sub.save()

    sub = Sub(name="Ham + Cheese" , size=BaseItem.SMALL , price=6.50 )
    sub.save()

    sub = Sub(name="Ham + Cheese" , size=BaseItem.LARGE , price=7.95 )
    sub.save()

    sub = Sub(name="Meatball" , size=BaseItem.SMALL , price=6.50 )
    sub.save()

    sub = Sub(name="Meatball" , size=BaseItem.LARGE , price=7.95 )
    sub.save()

    sub = Sub(name="Tuna" , size=BaseItem.SMALL , price=6.50 )
    sub.save()

    sub = Sub(name="Tuna" , size=BaseItem.LARGE , price=7.95 )
    sub.save()

    sub = Sub(name="Turkey" , size=BaseItem.SMALL , price=7.50 )
    sub.save()

    sub = Sub(name="Turkey" , size=BaseItem.LARGE , price=8.50 )
    sub.save()

    sub = Sub(name="Chicken Parmigiana" , size=BaseItem.SMALL , price=7.50 )
    sub.save()

    sub = Sub(name="Chicken Parmigiana" , size=BaseItem.LARGE , price=8.50 )
    sub.save()

    sub = Sub(name="Eggplant Parmigiana" , size=BaseItem.SMALL , price=6.50 )
    sub.save()

    sub = Sub(name="Eggplant Parmigiana" , size=BaseItem.LARGE , price=7.95 )
    sub.save()

    sub = Sub(name="Steak" , size=BaseItem.SMALL , price=6.50 )
    sub.save()

    sub = Sub(name="Steak" , size=BaseItem.LARGE , price=7.95 )
    sub.save()

    sub = Sub(name="Steak + Cheese" , size=BaseItem.SMALL , price=6.95 )
    sub.save()

    sub = Sub(name="Steak + Cheese" , size=BaseItem.LARGE , price=8.50 )
    sub.save()

    sub = Sub(name="Sausage, Peppers & Onions" , size=BaseItem.LARGE , price=8.50 )
    sub.save()

    sub = Sub(name="Hamburger" , size=BaseItem.SMALL , price=4.60 )
    sub.save()

    sub = Sub(name="Hamburger" , size=BaseItem.LARGE , price=6.95 )
    sub.save()

    sub = Sub(name="Cheeseburger" , size=BaseItem.SMALL , price=5.10 )
    sub.save()

    sub = Sub(name="Cheeseburger" , size=BaseItem.LARGE , price=7.45 )
    sub.save()

    sub = Sub(name="Fried Chicken" , size=BaseItem.SMALL , price=6.95 )
    sub.save()

    sub = Sub(name="Fried Chicken" , size=BaseItem.LARGE , price=8.50 )
    sub.save()

    sub = Sub(name="Veggie" , size=BaseItem.SMALL , price=6.95 )
    sub.save()

    sub = Sub(name="Veggie" , size=BaseItem.LARGE , price=8.50 )
    sub.save()



def addSubExtra():
    subextra = SubExtra(name="Cheese" , size=BaseItem.SMALL , price=0.50 )
    subextra.save()

    subextra = SubExtra(name="Cheese" , size=BaseItem.LARGE , price=0.50 )
    subextra.save()

    subextra = SubExtra(name="Mushrooms" , size=BaseItem.SMALL , price=0.50 )
    subextra.save()

    subextra = SubExtra(name="Mushrooms" , size=BaseItem.LARGE , price=0.50 )
    subextra.save()

    subextra = SubExtra(name="Green Peppers" , size=BaseItem.SMALL , price=0.50 )
    subextra.save()

    subextra = SubExtra(name="Green Peppers" , size=BaseItem.LARGE , price=0.50 )
    subextra.save()

    subextra = SubExtra(name="Onions" , size=BaseItem.SMALL , price=0.50 )
    subextra.save()

    subextra = SubExtra(name="Onions" , size=BaseItem.LARGE , price=0.50 )
    subextra.save()





def addPasta():
    pasta = Pasta(name="Baked Ziti w/Mozzarella" , price=6.50 )
    pasta.save()

    pasta = Pasta(name="Baked Ziti w/Meatballs" , price=8.75 )
    pasta.save()

    pasta = Pasta(name="Baked Ziti w/Chicken" , price=9.75 )
    pasta.save()




def addSalad():
    salad = Salad(name="Garden Salad" , price=6.25 )
    salad.save()

    salad = Salad(name="Greek Salad" , price=8.25 )
    salad.save()

    salad = Salad(name="Antipasto" , price=8.25 )
    salad.save()

    salad = Salad(name="Salad w/Tuna" , price=8.25 )
    salad.save()





