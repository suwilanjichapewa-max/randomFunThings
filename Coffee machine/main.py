from menu import MENU
from menu import resources

waterOg = resources["water"]
MilkOg = resources["milk"]
CoffeeOg = resources["coffee"]
bank = 0

valid_options = ["espresso", "latte", "cappuccino", "report", "off"]
on = True
while on:
    while True:
        try:
            decision = input("What would you like? (espresso/latte/cappuccino): ").lower()
            
            if decision in valid_options:
                #print(f"Great! One {decision} coming up.")
                break # Exit the loop if valid
            else:
                print("Sorry, we don't have that. Please choose espresso, latte, or cappuccino.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            exit()

    if decision == "espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]
        
        if waterOg <= water:
             print("Not enough water!")
        if CoffeeOg <= coffee:
             print("Not enough coffee!")
            
        else:
            waterOg -= water
            CoffeeOg -= coffee
            print("Here's your cappuccino")
            print(f"current water: {waterOg}")
            print(f"current milk: {MilkOg}")
            print(f"current coffee: {CoffeeOg}")   

    elif decision == "latte":
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        
        if waterOg <= water:
             print("Not enough water!")
        if CoffeeOg <= coffee:
             print("Not enough coffee!")
        if MilkOg <= milk:
             print("Not enough milk!")
            
        else:
            waterOg -= water
            MilkOg -= milk
            CoffeeOg -= coffee
            print("Here's your cappuccino")
            print(f"current water: {waterOg}")
            print(f"current milk: {MilkOg}")
            print(f"current coffee: {CoffeeOg}")   

    elif decision == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        
        if waterOg <= water:
             print("Not enough water!")
        if CoffeeOg <= coffee:
             print("Not enough coffee!")
        if MilkOg <= milk:
             print("Not enough milk!")
            
        else:
            waterOg -= water
            MilkOg -= milk
            CoffeeOg -= coffee
            print("Here's your cappuccino")
            print(f"current water: {waterOg}")
            print(f"current milk: {MilkOg}")
            print(f"current coffee: {CoffeeOg}") 

    elif decision == "report":
        print(f"current water: {waterOg}")
        print(f"current milk: {MilkOg}")
        print(f"current coffee: {CoffeeOg}")
  
    elif decision == "off":
        print("Goodbye!")
        on = False