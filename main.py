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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def check_resources(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][ingredient] > resources[ingredient]:
            print("Sorry there is not enough " + ingredient)
            return False
    return True


def insert_coin():
    print("Please insert coins.")
    quarter = input("How many quarters?")
    dime = input("How many dimes?")
    nickle = input("How many nickles?")
    pennie = input("How many pennies?")
    return int(quarter) * 0.25 + int(dime) * 0.1 + int(nickle) * 0.05 + int(pennie) * 0.01


def check_coin(coin_inserted, coffee):
    if coin_inserted < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    global money
    money += MENU[action]["cost"]
    return True


def make_coffee(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
    print("Here is your " + coffee + ". Enjoy!.")


while True:
    print("What would you like?")
    action = input()

    if action == "off":
        print("turning off the machine")
        break
    elif action == "report":
        print("Water: " + str(resources["water"]) + "ml", "\nMilk: " + str(resources["milk"]) + "ml", "\nCoffee: " + str(resources["coffee"]) + "ml", "\nMoney: $" + str(money))
    else:
        if check_resources(action):
            coin = insert_coin()
            if check_coin(coin, action):
                make_coffee(action)
