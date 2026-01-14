import item_module as i
from tabulate import tabulate


class Room:
    
    def __init__(self, name, item):
        self.name = name
        self.item = item
        

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
        print(f"Your in the {self.map[self.row][self.col].name}")

    def look_for_items(self):
        #sub menu
        while True:#while loop
            if self.map[self.row][self.col].item != None:#makes sure items are in the room
                print(f"Here are the items in the {self.map[self.row][self.col].name}:")
                items = self.map[self.row][self.col].item#gets dict
                for item in items.keys():#prints out items
                    print(f" - {item}, Capacity : {items[item].capacity}")
                print(" - Back")#go back to main menu
                choice_item = input("Wich one do you want:")# gets choice form player
                if choice_item in items.keys():#checks if choice is vaild
                    self.add_item(choice_item)#add item to inventory
                    del self.map[self.row][self.col].item[choice_item]#del item form dict
                elif choice_item == "Back":
                    break
                else:
                    print("Not a vaild choice")
            else:
                print("There are no items in this room")
                break
            
    def add_item(self, item):
        if len(self.inventory) < self.capacity:#checks if item fits in inventory
            print(f"You added a {item} to you inventory.")
            self.inventory.append(item)
            self.capacity = self.capacity - item.capacitcity
        else:
            print(f"Sorry your inventory is already full.")

    def remove_item(self, item):
        if item in self.inventory:
            print(f"You removed a {item} from your inventory.")
            self.inventory.remove(item)
        else:
            print(f"Sorry their are no {item}s in your inventory.")

    def view_inventory(self):
        if len(self.inventory) > 0:
            print("Inventory:")
            for item in self.inventory:
                print(f" - {item.name}, Capacity : {item.capacity}")
            print(f"Capacity left: {self.capacity}")
        else:
            print(f"Your Inventory is empty.")
    
    def view_map(self):
        print(tabulate(self.map, tablefmt="simple"))
        print(f"Your in the {self.map[self.row][self.col].name}")


            

kitchen = Room("kitchen", {i.knife.name : i.knife, i.pan.name :i.pan, 
                           i.spatula.name : i.spatula} )
bedroom1  = Room("Master Bedroom", {i.blanket.name : i.blanket, 
                                    i.teddy_bear.name :i.teddy_bear, 
                                    i.gum.name :i.gum} )
hallway  = Room("Hallway", None)
living_room  = Room("Living_room",{i.pillow.name : i.pillow, 
                                   i.lamp.name :i.lamp, 
                                   i.battries.name : i.battries} )
dining_room  = Room("Dinig_room", {i.fork.name : i.fork, 
                                   i.spoon.name :i.spoon, 
                                   i.plate.name :i.plate})
garage = Room("Garage", {i.hammer.name : i.hammer, 
                         i.duct_tape.name :i.duct_tape, 
                         i.screwdriver.name :i.screwdriver})
bunker_entrence  = Room("bunker_entrence", None)
foyer  = Room("foyer", None)
bathroom = Room("bathroom",{i.plunger.name :i.plunger, 
                            i.toothpaste.name :i.toothpaste, 
                            i.mouthwash.name :i.mouthwash})
bedroom2  = Room("Bedroom", {i.teddy_bear.name :i.t_shirt, 
                             i.action_figure.name :i.action_figure, 
                             i.candy_bar.name :i.candy_bar})

the_house = [[bedroom1, bunker_entrence, kitchen],
           [hallway, hallway, dining_room],
           [bedroom2, hallway, living_room],
           [garage , foyer, bathroom  ]]
    
def playing():
    print("You turn on the tv to see BREAKING NEWS!")
    print("CHERNOBAL IS ABOUT TO EXPLODE!")
    print("You quickly remeber the bunker you have that should protect you" \
    "form the blast. But when you get in your bunker") 
    print("you relize that the bunker is in complete disarray!")
    print("Quickly, you need to find whatever" \
    " you can in your house to fix it up!")
    print("")
    while True:
        options = ["move", "look at inventory", "look for items", "view map"]
        print("What would you like to do?")
        for option in options:
            print(f"- {option.title()}")
        choice_menu = input("choice: ").lower()
        if choice_menu == options[0]:
            player.movement()
        elif choice_menu == options[1]:
           player.view_inventory()
        elif choice_menu == options[2]:
           player.look_for_items()
        elif choice_menu == options[3]:
            player.view_map()
        else:
            print("sorry that was not a vaild choice")  

player = Player(the_house)

playing()