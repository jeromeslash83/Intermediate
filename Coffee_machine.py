MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def check_resources(coffee_type):
    """Checks if the resources in the machine are sufficient for the given order."""
    sub_water = resources['water'] - MENU[coffee_type]['ingredients']['water']
    sub_milk = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
    sub_coffee = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
    if sub_water >= 0 and sub_milk >= 0 and sub_coffee >= 0:
        return True
    else:
        return False


def execute_order(type_of_order):
    """Converts the menu ingredients to manageable variables"""
    global resources
    resources['water'] -= MENU[type_of_order]['ingredients']['water']
    resources['milk'] -= MENU[type_of_order]['ingredients']['milk']
    resources['coffee'] -= MENU[type_of_order]['ingredients']['coffee']


def add_money():
    quarter = (0.25 * int(input("How many quarters?\n")))
    dime = (0.1 * int(input("How many dimes?\n")))
    nickel = (0.05 * int(input("How many nickles?\n")))
    penny = (0.01 * int(input("How many pennies?\n")))
    total = quarter + dime + nickel + penny
    return total


while is_enough:
    order = input("What would you like? (espresso/latte/cappuccino):\n").lower()

    if order == 'report':
        resources_left()
    elif order == 'off':
        is_enough = False
    else:
        if check_resources(order):
            execute_order(order)
            total_money = add_money()
            if total_money - MENU[order]['cost'] < 0:
                print("That's not enough money.Money refunded")
            else:
                change = round(((MENU[order]['cost']) - (total_money)), 2)
                profit += total_money
                print(f"Here's ${change} in change.")
                print(f"Here's your {order}. Enjoy!")
        else:
            print("Sorry we don't have enough ingredients. Try again later.")
            is_enough = False
