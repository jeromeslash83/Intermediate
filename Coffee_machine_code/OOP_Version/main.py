from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resources = CoffeeMaker()
my_menu = Menu()
money = MoneyMachine()
is_on = True

while is_on:
    order = input(f"What would you like? {my_menu.get_items()} \n").lower()
    if order == 'report':
        resources.report()
        money.report()
    elif order == 'off':
        is_on = False
    else:
        if resources.is_resource_sufficient(my_menu.find_drink(order)) and money.make_payment(my_menu.find_drink(order).cost):
           resources.make_coffee(my_menu.find_drink(order))
        else:
            print('Please select a different order.')
