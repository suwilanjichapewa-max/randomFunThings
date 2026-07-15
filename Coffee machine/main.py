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
    print("Here's your espresso")
    print(f"current water: {waterOg}")
    print(f"current milk: {MilkOg}")
    print(f"current coffee: {CoffeeOg}")

elif decision == "latte":
    water = MENU["latte"]["ingredients"]["water"]
    milk = MENU["latte"]["ingredients"]["milk"]
    coffee = MENU["latte"]["ingredients"]["coffee"]
    
    waterOg -= water
    MilkOg =- milk
    CoffeeOg -= coffee
    print("Here's your latte")
    print(f"current water: {waterOg}")
    print(f"current milk: {MilkOg}")
    print(f"current coffee: {CoffeeOg}")

elif decision == "cappuccino":
    water = MENU["cappuccino"]["ingredients"]["water"]
    milk = MENU["cappuccino"]["ingredients"]["milk"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    
    waterOg -= water
    MilkOg =- milk
    CoffeeOg -= coffee
    print("Here's your cappuccino")
    print(f"current water: {waterOg}")
    print(f"current milk: {MilkOg}")
    print(f"current coffee: {CoffeeOg}")
