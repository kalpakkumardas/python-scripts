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

def is_resource_sufficient(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

def process_coins():
  print("Please insert coins")
  total = int(input("How many quaters? : "))*0.25
  total += int(input("How many dimes? : "))*0.1
  total += int(input("How many nickles? : "))*0.05
  total += int(input("How many pennies? : "))*0.01
  return total

def is_transaction_successful(money_received, drink_cost):
  if money_received >= drink_cost:
    change = round(money_received-drink_cost,2)
    print(f"Here is ${change} in change. ")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry that's not enough monet. Money has been refunded.")

def make_coffee(drink_name,order_ingredients):
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]

  print(f"Here is your {drink_name}")



is_on = True
while is_on:
 choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
 if choice == "off":
   is_on = False
 elif choice == "report":
   print(f"Water: {resources['water']}ml")
   print(f"Milk: {resources['milk']}ml")
   print(f"Coffee: {resources['coffee']}ml")
   print(f"Money: ${profit}")
 else:
    drink = MENU[choice]
    if is_resource_sufficient(drink["ingredients"]):
      payment = process_coins()
      if is_transaction_successful(payment,drink["cost"]):
        make_coffee(choice,drink['ingredients'])





   