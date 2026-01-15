#ONLY FOR NIXON

import player as p #So you can you the items in the players inventory


def bunker_menu():
     #Here you need to get player inventory 
     while True:
        print("1. instructions ")
        print("2. go back to house")
        print("3. view bunker map options")


        choice = input("choose an option: ")
        if choice == "1":
             show_instructions()
        elif choice == "2":
             go_to_house()
        elif choice == "3":
             view_map()  
        else:
            print("invalid choice try again :(")
          


def show_instructions():
    print("---------- BUNKER INSTRUCTIONS ----------")
    print("you have too move through the rooms and do the right tasks with the right tool.")
    print("if you do not have the right tool go back to the house to look for it.")
    print("your goal is to complete all of your tasks and fix up the bunker so you survive!")
    print("---------- GOOD LUCK! ----------")
    input("\nPress Enter to go back to menu")

def go_to_house():
    pass

def view_map():
    pass

class Task:
    def __init__(self, description, required_item):
        self.description = description
        self.required_item = required_item

boiler_room_task = Task ("You have to fix the boiler its leaking gas!!!....", "wrench")
kitchen_task = Task ("You have to fix the hole in the kitchen ceiling....", "special gum")
bedroom_task = Task ("Theres a hole in the wall....","wood")
hallway_task = Task ("Theres a leaking pipe you gotta take apart the metal wall to reach the leak","screw driver")
bathroom_task = Task ("the light is not working you gotta fix the wires", "wire cutters")    

class Room:
    def __init__(self, name, description, task):
        self.name = name
        self.description = description
        self.task = task
    

    def __str__(self):
        return self.name.title()


boiler_room = Room ("boiler room", "the boiler is broken and you need to fix it because its getting really cold...", boiler_room_task)
kitchen = Room ("kitchen", "the kitchen has a hole in the ceiling .......", kitchen_task)
bedroom = Room ("bedroom", "the bedroom wall has a crack in  it.......", bedroom_task)
hallway = Room ("hallway", "the hallway has a leaking pipe......", hallway_task )
bathroom = Room ("bathroom", "the light is broken........", bathroom_task)
entrence = Room ("entrence","the entrence is ", None)

map = [[bathroom, boiler_room],
       [entrence, kitchen],
       [hallway, bedroom]]


class Storage:
    def __init__(self, name, capacity):
        self.name = name
        self.inventory = [ ]
        self.capacity = capacity
        
    def view_inventory(self):
        if len(self.inventory) > 0:
            print(f" {self.name.title()} Inventory:")
            for item in self.inventory:
                print(f" - {item}")
        else:
            print(f"your {self.name} is empty.")
            
    def remove_item(self, item):
        if item in self.inventory:
            print(f"You removed a {item} from your {self.name}. ")
            self.inventory.remove(item)
        else:
            print(f" Sorry their are no {item}s in your {self.name}. ")





backpack = Storage("backpack",3)
backpack.view_inventory()
backpack.add_item("wrench")

print(map[0][1])
print(map[0][1].description)


