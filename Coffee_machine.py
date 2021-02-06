MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_enough = True


def resources_left():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")


def check_resources(type):
    """Checks if the resources in the machine are sufficient for the given order."""
    sub_water = resources['water'] - MENU[type]['ingredients']['water']
    sub_milk = resources['milk'] - MENU[type]['ingredients']['milk']
    sub_coffee = resources['coffee'] - MENU[type]['ingredients']['coffee']
    if sub_water > 0 or sub_milk > 0 or sub_coffee > 0:
        return True
    else:
        return False


def execute_order(type_of_order):
    """Converts the menu ingredients to manageable variables"""
    global resources
    resources['water'] -= MENU[type_of_order]['ingredients']['water']
    resources['milk'] -= MENU[type_of_order]['ingredients']['milk']
    resources['coffee'] -= MENU[type_of_order]['ingredients']['coffee']


order = input("What would you like? (espresso/latte/cappuccino):\n")


if check_resources(order):
    execute_order(order)
    print(resources)
