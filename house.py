class Room:
    
    def __init__(self,  name):
        self.name = name
        

    def __str__(self):
        return self.name.title()
    
kitchen = Room("kitchen")
bedroom  = Room("Bedroom")
hallway  = Room("Hallway")
living_room  = Room("Living_room")
dining_room  = Room("Dinig_room")
garage = Room("Garage")
bunker_entrence  = Room("bunker_entrence")
foyer  = Room("foyer")
bathroom = Room("bathroom")


the_house = [[bedroom, bunker_entrence, kitchen],
           [hallway, hallway, dining_room    ],
           [bedroom, hallway, living_room    ],
           [garage , foyer, bathroom  ]]