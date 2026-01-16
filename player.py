#Actually a combaintion of the player code and the house code, and is all the code for the first hafe of the game.


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
        #player loction to start with
        self.row = 3
        self.col = 1
        #givinig it the map
        self.map = map
        #player inventory and capacity
        self.inventory = []
        self.capacity = 15

    def movement(self):
        # Sub Men
        movement_options = ["North", "South", "East", "West" ]#different direction options
        print("\nWhere would you like to go?")
        for option in movement_options:
            print(f" - {option}")#printing out options
        choice = input("choice: ")#gets player choice
        #move you in dierction of your choice
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
            print("Sorry thats not a vaild choice.")
        print(f"You're in the {self.map[self.row][self.col].name}")#prints wich room you're in

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
                break#goes back to main menu
            
    def add_item(self, item):
        if len(self.inventory) < self.capacity:#checks if item fits in inventory
            print(f"You added a {item} to you inventory.")
            self.inventory.append(item)#adds item to inventory
            self.capacity = self.capacity - item.capacitcity#remove room in inventory base off of capicity of item
        else:
            print(f"Sorry your inventory is already full.")
    
    #not currently in use 
    def remove_item(self, item):
        if item in self.inventory:
            print(f"You removed a {item} from your inventory.")
            self.inventory.remove(item)
        else:
            print(f"Sorry their are no {item}s in your inventory.")

    def view_inventory(self):
        if len(self.inventory) > 0:#cheks if there is somthing in inventory
            print("Inventory:")
            for item in self.inventory:
                print(f" - {item.name}, Capacity : {item.capacity}")#prints out all items and there capcity
            print(f"Capacity left: {self.capacity}")#prints remaining sapce left in inventory
        else:
            print(f"Your Inventory is empty.")
    
    def view_map(self):
        print(tabulate(self.map, tablefmt="simple"))#tabulates map array 
        print(f"Your in the {self.map[self.row][self.col].name}")#prints the room your in


            
##creating rooms
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
#creating map
the_house = [[bedroom1, bunker_entrence, kitchen],
           [hallway, hallway, dining_room],
           [bedroom2, hallway, living_room],
           [garage , foyer, bathroom  ]]
    
def playing():
    #intro
    print("You turn on the tv to see BREAKING NEWS!")
    print("CHERNOBAL IS ABOUT TO EXPLODE!")
    print("You quickly remeber the bunker you have that should protect you" \
    "form the blast. But when you get in your bunker") 
    print("you relize that the bunker is in complete disarray!")
    print("Quickly, you need to find whatever" \
    " you can in your house to fix it up!")
    print("")
    while True:#Main menu
        options = ["move", "look at inventory", "look for items", "view map"]#Menu options
        print("What would you like to do?")
        for option in options:
            print(f"- {option.title()}")#printing out options
        if player.row == 0  and player.col == 1:
            print("- Go to bunker")#giving option to go to bunker if one bunker 
        choice_menu = input("choice: ").lower()#getting choice form player
        if choice_menu == options[0]:
            player.movement()#movement fuction
        elif choice_menu == options[1]:
           player.view_inventory()#view inventory fuction
        elif choice_menu == options[2]:
           player.look_for_items()#
        elif choice_menu == options[3]:
            player.view_map()
        elif choice_menu == ("Go to bunker").lower():
            break#ends this loop/menu
        else:
            print("sorry that was not a vaild choice")  

player = Player(the_house)#creating player

playing()