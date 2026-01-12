class Room:
    
    def __init__(self, name, items):
        self.name = name
        self.item = items
        

    def __str__(self):
        return self.name.title()

class Player:
    
    def __init__(self, map):
        self.row = 3
        self.col = 1
        self.map = map
        self.inventory = []
        self.capacity = 5

    def movement(self):
        # Sub Men
        movement_options = ["North", "South", "East", "West" ]
        print("\nWhere would you like to go?")
        for option in movement_options:
            print(f" - {option}")
        choice = input("choice: ")
        if choice == "North":
            if self.row > 0:
                self.row -= 1
        elif choice == "South":
            if self.row < 3:
                self.row += 1
        elif choice == "East":
            if self.col > 0:
                self.col -= 1
        elif choice == "West":
            if self.col < 3:
                self.col += 1
        else:
            print("Sorry you can not move that way.")
        print(self.row, self.col)

    def look_for_items(self):
        while True:
            if self.map[self.row][self.col].item != None: 
                print("Here are the items in this room:")
                items = self.map[self.row][self.col].item
                for item in items:
                    print(f" - {item}")
                print(" - Back")
                choice_item = input("Wich one do you want:")
                if choice_item in self.map[self.row][self.col].item:
                    self.add_item(choice_item)
                elif choice_item == "Back":
                    break
                else:
                    print("Not a vaild choice")
            else:
                print("There are no items in this room")

    def add_item(self, item):
        if len(self.inventory) < self.capacity:
            print(f"You added a {item} to you inventory.")
            self.inventory.append(item)
        else:
            print(f"Sorry your inventory is already full.")

     #def remove_item(self, item):
        #if item in self.inventory:
            #print(f"You removed a {item} from your {self.name}.")
            #self.inventory.remove(item)
        #else:
            #print(f"Sorry their are no {item}s in your {Net}.")

    
            

kitchen = Room("kitchen", ["Knife","Pan","Spatula"])
bedroom1  = Room("Bedroom", ["Blanket","Teddy Bear","Gum"])
hallway  = Room("Hallway", None)
living_room  = Room("Living_room", ["Pillow","Lap","Battries"])
dining_room  = Room("Dinig_room", ["Fork","Spoon","Plate"])
garage = Room("Garage", ["Hammer","Duct tape","Screwdriver"])
bunker_entrence  = Room("bunker_entrence", None)
foyer  = Room("foyer", None)
bathroom = Room("bathroom", ["Plunger","Toothpaste","Mouthwash"])
bedroom2  = Room("Bedroom", ["T-shirt","Action figure","Candy bar"])

the_house = [[bedroom1, bunker_entrence, kitchen],
           [hallway, hallway, dining_room    ],
           [bedroom2, hallway, living_room    ],
           [garage , foyer, bathroom  ]]
    
def playing():
    while True:
        options = ["Move", "Look at inventory", "Look for items"]
        print("What would you like to do?")
        for option in options:
            print(f" - {option}")
        choice_menu = input("choice: ")
        if choice_menu == options[0]:
            player.movement()
        elif choice_menu == options[1]:
           player.view_inventory()
        elif choice_menu == options[2]:
           player.look_for_items()
        else:
            print("sorry that was not a vaild choice")  

player = Player(the_house)
playing()