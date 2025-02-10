class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # What methods will you need?

    # updating a computer's price
    def update_price(self, new_price):
        self.price = new_price

    # updating a computer's OS
    def update_os(self, new_os):
        self.operating_system = new_os
    
    # storing information about a computer
    def __str__(self):
        return f"{self.description} ({self.year_made}), {self.processor_type}, {self.memory}GB RAM, {self.hard_drive_capacity}GB, {self.operating_system}, ${self.price}"
    
