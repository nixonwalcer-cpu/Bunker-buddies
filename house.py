#No longer in use, outdated

class Room:
    
    def __init__(self,  name, item):
        self.name = name
        self.item = item
        

    def __str__(self):
        return self.name.title()
  
kitchen = Room("kitchen", "Knife")
bedroom  = Room("Bedroom", "Blanket")
hallway  = Room("Hallway", None)
living_room  = Room("Living_room", "Pillow")
dining_room  = Room("Dinig_room", "Fork")
garage = Room("Garage", "Hammer")
bunker_entrence  = Room("bunker_entrence", None)
foyer  = Room("foyer", None)
bathroom = Room("bathroom", "Plunger")


the_house = [[bedroom, bunker_entrence, kitchen],
           [hallway, hallway, dining_room    ],
           [bedroom, hallway, living_room    ],
           [garage , foyer, bathroom  ]]

print(bathroom)