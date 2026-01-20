#########################################################################################
# Title:Item
# Date:1/16/26
# Version: I don't know we forgot to count
#########################################################################################
"""
Item class and creating all items
"""
#########################################################################################

class Item:
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = int(capacity)

#creating items
knife = Item("Kinfe", 2)
pan = Item("Pan", 3)
spatula = Item("Spatula", 2)
blanket = Item("Blanket", 2)
teddy_bear = Item("Teddy Bear", 2)
gum = Item("Gum", 2)
pillow = Item("Pillow", 3)
lamp = Item("Lamp", 3)
battries = Item("Battries", 1)
fork = Item("Fork", 1)
spoon = Item("Spoon", 1)
plate = Item("Plate", 3)
hammer = Item("Hammer", 2)
duct_tape = Item("Duct Tape", 1)
screwdriver = Item("Screwdriver", 2)
plunger = Item("Plunger", 3)
toothpaste = Item("Toothpaste", 1)
mouthwash = Item("Mouthwash", 2)
t_shirt = Item("T-shirt", 2)
action_figure = Item("Action figure", 2)
candy_bar = Item("Candy bar", 1)


