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

print(menu)

askOrder = """
***********************************
** What would you like to order? **
***********************************
"""

def customerOrder():
  print(askOrder)
  ongoingOrder = True
  cust_order = {}
  while ongoingOrder:
    order = input("> ")
    if order == "quit":
      ongoingOrder = False
    else:
      if order in cust_order.keys():
        cust_order[order] += 1
      else:
        cust_order[order] = 1
      numOfItem = cust_order[order]
      if numOfItem == 1:
        orders = "order"
      else:
        orders = "orders"
      order_format = f"{numOfItem} {orders} of {order} have been added to your meal"
      print(order_format)

customerOrder()
