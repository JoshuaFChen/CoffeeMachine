from menu import Menu
from money_machine import MoneyMachine
import initial_data


class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = initial_data.resources
        self.is_on = False
        self.money_machine = MoneyMachine()
        self.menu = Menu()

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def run(self):
        self.is_on = True
        while self.is_on:
            options = self.menu.get_items()
            choice = input(f"What would you like? ({options}): ")
            if choice == "off":
                self.is_on = False
            elif choice == "report":
                self.report()
                self.money_machine.report()
            else:
                drink = self.menu.find_drink(choice)
                if self.is_resource_sufficient(drink) and self.money_machine.make_payment(drink.cost):
                    self.make_coffee(drink)
