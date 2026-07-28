from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

decision = input("What would you like?? (espresso/latte/cappuccino): ").lower()
cc = Menu()
aa = cc.get_items()

for i in aa:
    print(i)