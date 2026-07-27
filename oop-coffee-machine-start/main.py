from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

decision = input("What would you like?? (espresso/latte/cappuccino): ").lower()
cc = Menu.get_items()
