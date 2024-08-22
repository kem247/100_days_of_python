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
    "money": 0
}


#TODO deduct resources
def deduct_resources(u_input):
    if u_input == 'cappuccino' or u_input == 'latte' or u_input == 'espresso':
        resources['water'] -= MENU[u_input]["ingredients"]["water"]
        resources['coffee'] -= MENU[u_input]["ingredients"]["coffee"]
        if 'milk' in MENU[u_input]["ingredients"]:
            resources['milk'] -= MENU[u_input]["ingredients"]["milk"]
        else:
            resources['milk'] = resources['milk']
    else:
        return (f" Water: {resources['water']}ml\n Milk: {resources['milk']}ml"
                f"\n Coffee: {resources['coffee']}g\n Money: ${resources['money']}")


#TODO check resources
def check_resources(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False

        return True

#TODO calculate coins
def succesful_transaction(payment, user_drink):
    cost = MENU[user_drink]["cost"]
    if int(payment) < cost:
        resources["money"]  += 0
        return "Sorry that's not enough money. Money refunded."
    elif int(payment) == cost:
        resources["money"] += payment
        deduct_resources(user_drink)
        return f"Here is your {user_drink} ☕. Enjoy!"
    elif int(payment) > cost:
        change = round((int(payment) - cost), 2)
        resources["money"] += cost
        deduct_resources(user_drink)
        return f"Here is ${change} in change. Here is your {user_drink} ☕. Enjoy!"


def calculate_coins(quarters, dimes, nickles, pennies):
    money = 0
    if quarters:
        money += int(quarters) * .25
    if dimes:
        money += int(dimes) * .10
    if nickles:
        money += int(nickles) * .05
    if pennies:
        money += int(pennies) * .01
    return round(money, 2)


#TODO prompt user
game = True
while game:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
 #TODO process coins
    if user_input == 'off':
        game = False
#TODO print report
    elif user_input == 'report':
        print(deduct_resources(user_input))
    else:
        drink = MENU[user_input]
        check = check_resources(drink["ingredients"])
        if check:
            print("Please insert coins.")
            quarters = input("How many quarters?: ")
            dimes = input("How many dimes?: ")
            nickles = input("How many nickles?: ")
            pennies = input("How many pennies?: ")
            payment = calculate_coins(quarters, dimes, nickles, pennies)
            print(succesful_transaction(payment, user_input))
        else:
            print(check)

