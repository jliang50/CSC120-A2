from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []


    # What methods will you need?
    # add a new Computer to the inventory
    def buy(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price): 
        # 1. call Computer(...) constructor to create a new Computer instance
        new_computer = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
        # 2. call inventory.append(...) to add the new Computer instance to the inventory
        self.inventory.append(new_computer)
        return len(self.inventory) - 1  # return the index of the newly added computer
    
    # remove a computer from the inventory by item_id
    def sell(self, item_id):
        if 0 <= item_id < len(self.inventory):
            self.inventory.pop(item_id)
            print(f"Item {item_id} sold!")
        else:
            print(f"Item {item_id} not found. Please select another item to sell.")

    # update the price/OS of a computer in the inventory
    def refurbish(self, item_id, new_os=None):
        if 0 <= item_id < len(self.inventory):
            computer = self.inventory[item_id] # locate the computer
            if computer.year_made < 2000:
                computer.update_price(0)  # too old to sell, donation only
            elif computer.year_made < 2012:
                computer.update_price(250)  # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                computer.update_price(550)  # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000)  # recent stuff

            if new_os:
                computer.update_os(new_os)  # update details after installing new OS
        else:
            print(f"Item {item_id} not found. Please select another item to refurbish.")

    # printing the inventory
    def print_inventory(self):
        if self.inventory:
            for item_id, computer in enumerate(self.inventory):
                print(f"Item ID: {item_id} : {computer}")
        else:
            print("No inventory to display.")
