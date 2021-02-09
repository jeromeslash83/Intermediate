from Menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resources = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
is_on = True

while is_on:
    order = input(f"What would you like? {menu.get_items()} \n").lower()
    if order == 'report':
        resources.report()
        money.report()
    elif order == 'off':
        is_on = False
    else:
        choice = menu.find_drink(order)
        if resources.is_resource_sufficient(choice):
           money.make_payment(choice.cost)
           resources.make_coffee(choice)
        else:
            resources.is_resource_sufficient(choice)
            is_on = False






