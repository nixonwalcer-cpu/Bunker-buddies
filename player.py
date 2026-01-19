#########################################################################################
# Title:Player
# Date:1/16/26
# Version: I don't know we forgot to count
#########################################################################################
"""
The code for the houses map, the room classes in the house and the player class
"""
#########################################################################################
import item_module as i
from tabulate import tabulate

class Room:
    
    def __init__(self, name, item):
        self.name = name
        self.item = item
        

    def __str__(self):
        '''Retunrns the name of each room, for printing purposes'''
        return self.name.title()
    

class Player:
    
    def __init__(self, map):
        #Player loction
        self.row = 3
        self.col = 1

        #Player map
        self.map = map

        #Player inventory and capacity
        self.inventory = []
        self.capacity = 15

    def movement(self):
        # Sub Menu for movement
        '''Print a list of directions, gets player to select one, 
        then changer the row or coloum on the map base off of that choice.
        Will loop after unless seletion it "back", wich will retrune player
        to main menu'''
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
            print("Sorry thats not a vaild choice.")
        print(f"You're in the {self.map[self.row][self.col].name}")
    
    def look_for_items(self):
        #Sub menu for looking for items
        '''Gets the list of items of the room the player is currently in, prints them out,
        and gets the player to select one, then uses the add items function. It will then loop
        unless plyaer selects "back", wich will retunr them to the main menu'''
        while True:
            if self.map[self.row][self.col].item != None:
                print(f"Here are the items in the {self.map[self.row][self.col].name}:")
                items = self.map[self.row][self.col].item
                for item in items.keys():
                    print(f" - {item}, Capacity : {items[item].capacity}")
                print(" - Back")
                choice_item = input("Wich one do you want:")
                if choice_item in items.keys():
                    self.add_item(items[choice_item])
                    del self.map[self.row][self.col].item[choice_item]
                elif choice_item == "Back":
                    break
                else:
                    print("Not a vaild choice")
            else:
                print("There are no items in this room")
                break
    
    def add_item(self, item):
        #Add item function 
        '''Checks if player inventory is full, and if it isn't, will put the item attribute it got form
        the "Look for items" function, and adds it from the player inventory list'''
        if len(self.inventory) < self.capacity:
            print(f"You added a {item.name} to you inventory.")
            self.inventory.append(item)
            self.capacity = self.capacity - item.capacity
        else:   
            print(f"Sorry your inventory is already full.")
    
    
    def view_inventory(self):
        #Function to look at inventory
        '''Checks if there's somthing in the inventory, and if there is, print the item(s) name and capcity,
        and then what room in you inventory you have left'''
        if len(self.inventory) > 0:
            print("Inventory:")
            for item in self.inventory:
                print(f" - {item.name}, Capacity : {item.capacity}")
            print(f"Capacity left: {self.capacity}")
        else:
            print(f"Your Inventory is empty.")
    
    def view_map(self):
        #Function for looking at map
        '''Use tabulate to format the map correctly for printing, then prints the room your in'''
        print(tabulate(self.map, tablefmt = "simple"))
        print(f"Your in the {self.map[self.row][self.col].name}")


            
#Creating rooms
kitchen = Room("kitchen", {i.knife.name : i.knife, i.pan.name : i.pan, 
                           i.spatula.name : i.spatula} )

bedroom1  = Room("Master Bedroom", {i.blanket.name : i.blanket, 
                                    i.teddy_bear.name : i.teddy_bear, 
                                    i.gum.name : i.gum} )
hallway  = Room("Hallway", None)

living_room  = Room("Living_room",{i.pillow.name : i.pillow, 
                                   i.lamp.name : i.lamp, 
                                   i.battries.name : i.battries} )

dining_room  = Room("Dinig_room", {i.fork.name : i.fork, 
                                   i.spoon.name : i.spoon, 
                                   i.plate.name : i.plate})

garage = Room("Garage", {i.hammer.name : i.hammer, 
                         i.duct_tape.name : i.duct_tape, 
                         i.screwdriver.name : i.screwdriver})

bunker_entrence  = Room("bunker_entrence", None)

foyer  = Room("foyer", None)

bathroom = Room("bathroom",{i.plunger.name : i.plunger, 
                            i.toothpaste.name : i.toothpaste, 
                            i.mouthwash.name : i.mouthwash})

bedroom2  = Room("Bedroom", {i.teddy_bear.name : i.t_shirt, 
                             i.action_figure.name : i.action_figure, 
                             i.candy_bar.name : i.candy_bar})

#Creating map
the_house = [[bedroom1, bunker_entrence, kitchen],
             [hallway, hallway, dining_room],
             [bedroom2, hallway, living_room],
             [garage , foyer, bathroom  ]]


def playing():
    #Main game funtion
    '''Prints out and intro, then prints out different options the player can choose, makes the player give
    a selection, then goes to the function corrasponding to the selection''' 
    #Intro
    print('''You turn on the tv to see BREAKING NEWS!
    ---CHERNOBAL IS ABOUT TO EXPLODE!---
    You quickly remeber the bunker you have that should protect you 
    form the blast. But when you get in your bunker
    you relize that the bunker is in complete disarray!
    Quickly, you need to find whateveryou can in your house to fix it up!''')
    print("")
    #Main menu
    while True:
        options = ["move", "look at inventory", "look for items", "view map"]
        print("What would you like to do?")
        for option in options:
            print(f"- {option.title()}")
        if player.row == 0  and player.col == 1:
            print("- Go to bunker") 
        choice_menu = input("choice: ").lower()
        if choice_menu == options[0]:
            player.movement()
        elif choice_menu == options[1]:
           player.view_inventory()
        elif choice_menu == options[2]:
           player.look_for_items()
        elif choice_menu == options[3]:
            player.view_map()
        elif choice_menu == ("Go to bunker").lower():
            break
        else:
            print("sorry that was not a vaild choice")  


#Creating player
player = Player(the_house)

