# TODO: 1. Import the resources
from Resource import resources
from Resource import MENU

# TODO: Declare Global Variables
Water = resources['water']
Milk = resources['milk']
Coffee = resources['coffee']
Cost = 0.00

# TODO: User_Money
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


# TODO: 2. Print the Report
def report():
    print(f"Water: {Water}ml\nMilk: {Milk}ml\nCoffee: {Coffee}g\nCost: ${Cost}")


# TODO: 3. Take User Input for the Coffee
print("1.Espresso \n2.Latte \n3.Cappuccino \n4.Report \n5.Leave")
Returned_Money = 0.00

User_Input = int(input("What Would You Like to have: "))

while User_Input != 5:
    if User_Input == 1:
        if Water < MENU['espresso']['ingredients']['water']:
            print(f"Sorry insufficient Water")
        elif Coffee < MENU['espresso']['ingredients']['coffee']:
            print(f"Sorry insufficient Coffee")
        else:
            print("Please insert coins:")
            User_quarters = int(input("How many Quarters: "))
            User_dimes = int(input("How many Dimes: "))
            User_nickles = int(input("How many Nickles: "))
            User_pennies = int(input("How many Pennies: "))

            Total_quarters = quarters * User_quarters
            Total_dimes = dimes * User_dimes
            Total_nickles = nickles * User_nickles
            Total_pennies = pennies * User_pennies

            Total_Amount = Total_quarters + Total_dimes + Total_nickles + Total_pennies
            if Total_Amount < MENU['espresso']['cost']:
                print("Sorry that's not enough money. Money Refunded")
            else:
                Returned_Money = round(Total_Amount - MENU['espresso']['cost'], 2)
                Water -= MENU['espresso']['ingredients']['water']
                Coffee -= MENU['espresso']['ingredients']['coffee']
                Cost += MENU['espresso']['cost']
                print(f"Here is ${Returned_Money} in change.")
                print("Here is Your Espresso. Enjoy and Have a Nice Day.")
    elif User_Input == 2:
        if Water < MENU['latte']['ingredients']['water']:
            print(f"Sorry insufficient Water")
        elif Milk < MENU['latte']['ingredients']['milk']:
            print(f"Sorry insufficient Milk")
        elif Coffee < MENU['latte']['ingredients']['coffee']:
            print(f"Sorry insufficient Coffee")
        else:
            print("Please insert coins:")
            User_quarters = int(input("How many Quarters: "))
            User_dimes = int(input("How many Dimes: "))
            User_nickles = int(input("How many Nickles: "))
            User_pennies = int(input("How many Pennies: "))

            Total_quarters = quarters * User_quarters
            Total_dimes = dimes * User_dimes
            Total_nickles = nickles * User_nickles
            Total_pennies = pennies * User_pennies

            Total_Amount = Total_quarters + Total_dimes + Total_nickles + Total_pennies
            if Total_Amount < MENU['latte']['cost']:
                print("Sorry that's not enough money. Money Refunded")
            else:
                Returned_Money = round(Total_Amount - MENU['latte']['cost'], 2)
                Water -= MENU['latte']['ingredients']['water']
                Milk -= MENU['latte']['ingredients']['milk']
                Coffee -= MENU['latte']['ingredients']['coffee']
                Cost += MENU['latte']['cost']
                print(f"Here is ${Returned_Money} in change.")
                print("Here is Your Latte. Enjoy and Have a Nice Day.")
    elif User_Input == 3:
        if Water < MENU['cappuccino']['ingredients']['water']:
            print(f"Sorry insufficient Water")
        elif Milk < MENU['cappuccino']['ingredients']['milk']:
            print(f"Sorry insufficient Milk")
        elif Coffee < MENU['cappuccino']['ingredients']['coffee']:
            print(f"Sorry insufficient Coffee")
        else:
            print("Please insert coins:")
            User_quarters = int(input("How many Quarters: "))
            User_dimes = int(input("How many Dimes: "))
            User_nickles = int(input("How many Nickles: "))
            User_pennies = int(input("How many Pennies: "))

            Total_quarters = quarters * User_quarters
            Total_dimes = dimes * User_dimes
            Total_nickles = nickles * User_nickles
            Total_pennies = pennies * User_pennies

            Total_Amount = Total_quarters + Total_dimes + Total_nickles + Total_pennies
            if Total_Amount < MENU['cappuccino']['cost']:
                print("Sorry that's not enough money. Money Refunded")
            else:
                Returned_Money = round(Total_Amount - MENU['cappuccino']['cost'], 2)
                Water -= MENU['cappuccino']['ingredients']['water']
                Milk -= MENU['cappuccino']['ingredients']['milk']
                Coffee -= MENU['cappuccino']['ingredients']['coffee']
                Cost += MENU['cappuccino']['cost']
                print(f"Here is ${Returned_Money} in change.")
                print("Here is Your Cappuccino. Enjoy and Have a Nice Day.")
    elif User_Input == 4:
        report()
    elif User_Input == 5:
        exit()
    User_Input = int(input("What Would You Like to have: "))
print("Have a Nice Day Dear. See You Soon.")
# # TODO: espresso
# EWater = MENU['espresso']['ingredients']['water']
# ECoffee = MENU['espresso']['ingredients']['coffee']
# ECost = MENU['espresso']['cost']
#
#
# # TODO: Latte
# LWater = MENU['latte']['ingredients']['water']
# LMilk = MENU['latte']['ingredients']['milk']
# LCoffee = MENU['latte']['ingredients']['coffee']
# LCost = MENU['latte']['cost']
#
#
# # TODO: cappuccino
# CWater = MENU['cappuccino']['ingredients']['water']
# CMilk = MENU['cappuccino']['ingredients']['milk']
# CCoffee = MENU['cappuccino']['ingredients']['coffee']
# CCost = MENU['cappuccino']['cost']
