from menu import MENU
from menu import resources

waterOg = resources["water"]
MilkOg = resources["milk"]
CoffeeOg = resources["coffee"]
bank = 0

decision = input("What would you like? (espresso/latte/cappuccino): ").lower()

if decision == "espresso":
    water = MENU["espresso"]["ingredients"]["water"]
    #milk = MENU["espresso"]["ingredients"]["milk"]
    coffee = MENU["espresso"]["ingredients"]["coffee"]
    
    waterOg -= water
    #MilkOg =- milk
    CoffeeOg -= coffee

    print(f"current water: {waterOg}")
    print(f"current milk: {MilkOg}")
    print(f"current coffee: {CoffeeOg}")