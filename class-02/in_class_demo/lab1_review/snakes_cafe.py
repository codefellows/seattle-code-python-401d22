"""
When run, the program should print an intro message and the menu for the restaurant
The restaurant’s menu should include appetizers, entrees, desserts, and beverages.
The program should prompt the user for an order
When a user enters an item, the program should print an acknowledgment of their input
The program should tell the user how to exit
The program’s content should match included sample exactly
Actually, there’s one tiny spot that should be different - see if you can spot it.
The > character represents user input line and should be printed out with a trailing space.
"""

menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""

prompt="""
***********************************
** What would you like to order? **
***********************************
"""

orders = {}
continue_order = True
print(menu)

while continue_order:
    print(prompt)
    item = input("> ")
    if item == "quit":
        continue_order = False
        break
    if item not in orders:
        orders[item] = 1
        print(f'** 1 order of {item} has been added to your meal **')
    else:
        orders[item] +=1
        item_count = orders[item]
        print(f'** {item_count} orders of {item} have been added to your meal **')

