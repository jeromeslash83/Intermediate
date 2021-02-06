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

water = 0
milk = 0
coffee = 0
is_enough = True


def resources_left():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    

def check_resources(type):
    """Checks if the resources in the machine are sufficient for the given order."""
    sub_water = resources['water'] - type['ingredients']['water']
    sub_milk = resources['milk'] - type['ingredients']['milk']
    sub_coffee = resources['coffee'] - type['ingredients']['coffee']
    if sub_water or sub_milk or sub_coffee < 0:
        return False
    else:
        return True


order = input("What would you like? (espresso/latte/cappuccino):\n")
