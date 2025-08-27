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

# Machine on-off key
machine_on = True

sales = 0

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def calculate_coins():
    print("Please Insert Coins")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01

    return total

def process_transaction (coins_inserted, drink_cost):
    if coins_inserted < drink_cost:
        print("Sorry that's not enough money. Money us refunded")
        return 0, False
    else:
        global sales
        sales += drink_cost
        return round(coins_inserted - drink_cost, 2) , True

def update_resources(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]



while machine_on:
    # Prompt the user for their drink

    user_input = input("What would you like? (espresso/latte/cappuccino)").lower()

    if user_input == "off":
        machine_on = False
        break
    elif user_input == "report":
        print(f"Sales:{sales}")
        print(f"Water:{resources['water']}")
        print(f"Milk:{resources['milk']}")
        print(f"Coffee:${resources['coffee']}")
    else:
        if user_input in MENU:
            coffee_type = MENU[user_input]
            if check_resources(coffee_type["ingredients"]):
                coins_collected = calculate_coins()
                print(coins_collected)
                balance, enough_payment = process_transaction(coins_collected, coffee_type["cost"])
                if enough_payment:
                    update_resources(coffee_type["ingredients"])
                    print(f"Please have your {user_input}")
                    if balance > 0:
                        print(f"Kindly take your balance ${balance}. Have a great day")
        else:
            print("Invalid selection. Please try again.")
