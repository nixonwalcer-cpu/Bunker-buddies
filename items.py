import random

items = {"Hammer":"Garage",
         "Sicssors":"Kitchien"}



class Items:

    def __init__(self):
        self.room = items.values
        self.name = items.keys
    
    def __str__(self):
        return self.name.title()

item_type = random.choice(list(items))

print(item_type)