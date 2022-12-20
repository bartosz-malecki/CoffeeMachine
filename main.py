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


# TODO: 2. Check resources sufficient to make drink order.
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            return False
    return True


#


# TODO: 4. Process coins.
def insert_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# TODO: 5. Check if transaction is successful.
def is_transaction_successful(cost_operation):
    for item in cost_operation:
        if cost_operation[item] > insert_coins:
            print("no ok")


# TODO: 6. Make Coffee
turn_off = False

while not turn_off:
    # TODO: 3. Ask user what to do.
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 7. Turn off the Coffee Machine.
    if choice == "off":
        turn_off = True
    # TODO: 1. Print report of current resource values.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if choice == "espresso":
            insert_coins()
