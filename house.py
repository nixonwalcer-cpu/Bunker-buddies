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
garage= Room("Cellar")
bunker_entrence  = Room("bunker_entrence")
entrance_way  = Room("Entrance")
bathroom = Room("bathroom")


the_map = [[bedroom, bunker_entrence, kitchen],
           [hallway, hallway, dining_room    ],
           [bedroom, hallway, living_room    ],
           [garage , entrance_way, bathroom  ]]