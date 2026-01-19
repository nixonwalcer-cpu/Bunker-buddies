#ONLY FOR NIXON
import player as p

playing_bunker = True


class Storage:
    def __init__(self, name, capacity):
        self.name = name
        self.inventory = p.player.inventory
        self.capacity = p.player.capacity
       
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


def bunker_menu():
     while playing_bunker:
        print("1. instructions ")
        print("2. view bunker options")
        print("3. quit")
        choice = input("choose an option: ")
        if choice == "1":
            show_instructions()
        elif choice == "2":
            view_bunker_options()
        elif choice == "3":
            break
        else:
            print("invalid choice try again :(")
     print("Goodbye")    




def show_instructions():
    print("---------- BUNKER INSTRUCTIONS ----------")
    print("you have too move through the rooms and do the right tasks with the right tool.")
    print("if you do not have the right tool go back to the house to look for it.")
    print("your goal is to complete all of your tasks and fix up the bunker so you survive!")
    print("---------- GOOD LUCK! ----------")
    input("\nPress Enter to go back to menu")




def view_bunker_options():
    while True:
        print("1. go back to main bunker menu")
        print("2. view bunker map")
        print("3. move around bunker")
        choice = input("choose an option: ")
        if choice == "1":
            break
        elif choice == "2":
            view_bunker_map()
        elif choice == "3":
            move_around_bunker()
        else:
            print("invalid choice try again :(")


   
def view_bunker_map():
    print("~~~~~~~ BUNKER MAP ~~~~~~~")
    for row in bunker_map:
        for room in row:
            print(f"[{room.name.upper()}]", end=" ")
        print()  
    input("\nPress Enter to go back to menu")




def view_tasks():
    for row in bunker_map:
        for room in row:
            if room.task:
                status = "completed" if room.task.completed else "uncomplete"
                print(f"{room.name.title()}: {room.task.description} [{status}]")
    input("\nPress Enter to go back to menu")




def move_around_bunker():
    while True:
        current_room = bunker_map[player.row][player.col]
        print(f"you are in the {current_room.name}. ")
        print(current_room.description)
        print("\nDirections:")
        print("1. go back")
        print("use w a s d to move around the bunker")
        choice = input("> ")
        if choice == "1":
            return
        elif choice in ["w", "a", "s", "d"]:
            player.move(choice)
            current_room = bunker_map[player.row][player.col]
            print(f"you are in the {current_room.name}. ")
            print(current_room.description)
            if not current_room.task.completed:
                current_room.task.do_task(player)
               
        else:
            print("please use w, a, s, d to move around")




class Task:
    def __init__(self, description, required_item):
        self.description = description
        self.required_item = required_item
        self.completed = False


    def do_task(self, task_doer):
        print(self.description)
        while not self.completed:
            print("your inventory: ")
            task_doer.inventory.view_inventory()
            if len (task_doer.inventory.inventory) == 0:
                print("you have no items to complet this task")                      
                return                                                                  
            item = input("what item do you want to use?(or type 'back') ")
            if item == "back":
                print("you left the task")
            if item == self.required_item:
                print("You finished the task! go to the next task!!")
            self.completed = True
        else:
            print("WRONG ITEM. you have to use the right item to fix the bunker!")




boiler_room_task = Task ("You have to fix the boiler its leaking gas!!! what can patch a hole fast?", "duck tape")
kitchen_task = Task ("You have to fix the hole in the kitchen ceiling, what can cover the hole", "blanket")
bedroom_task = Task ("your bed is broken and the bed leg needs to be fixed","plunger")
hallway_task = Task ("Theres a leaking pipe you gotta take apart the metal wall to reach the leak","screwdriver")
bathroom_task = Task ("the light is not working you gotta fix the wires what can u use thats conductive?", "fork")    




class Room:
    def __init__(self, name, description, task):
        self.name = name
        self.description = description
        self.task = task
   
    def __str__(self):
        return self.name.title()




boiler_room = Room ("boiler room", "the boiler is broken and you need to fix it because its "
                    + "getting really cold", boiler_room_task)
kitchen = Room ("kitchen", "the kitchen has a hole in the ceiling", kitchen_task)
bedroom = Room ("bedroom", "the bedroom wall has a crack in it", bedroom_task)
hallway = Room ("hallway", "the hallway has a leaking pipe", hallway_task )
bathroom = Room ("bathroom", "the light is broken", bathroom_task)
entrence = Room ("entrence","the entrence is ", None)




bunker_map = [[bathroom, boiler_room],
              [entrence, kitchen],
              [hallway, bedroom]]




class Player:
    def __init__(self, name, row, col, my_map):
        self.name = name
        self.row = row
        self.col = col
        self.map = my_map
        self.inventory = Storage("Backpack", 15)
       
    def move(self, direction):
        if direction.lower() == "w":
            if self.row > 0:
                self.row -= 1
            else:
                print("You hit a wall try going in a different direction")
        elif direction.lower() == "s":
            if self.row < len(bunker_map)-1:
                self.row += 1
            else:
                print("You hit a wall try going in a different direction")
        elif direction.lower() == "a":
            if self.col > 0:
                self.col -= 1
            else:
                print("You hit a wall try going in a different direction")
        elif direction.lower() == "d":
            if self.col < len(bunker_map[self.row])-1:
                self.col += 1
            else:
                print("You hit a wall try going in a different direction")
        else:
            print("please use w, a, s, d to move ")


start_row = 1
start_col = 0
player = Player("Alex", start_row, start_col, bunker_map)



















