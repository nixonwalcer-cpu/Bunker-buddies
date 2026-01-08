class Player:
    
    def __init__(self):
        self.row = 3
        self.col = 1
    
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

class Inventory:
    
    def __init__(self):
        self.inventory = []
        
    
    def view_inventory(self):
        if len(self.inventory) > 0:
            print("Inventory:")
            for item in self.inventory:
                print(f" - {item}")
        else:
            print(f"Your Inventory is empty.")
    
    #def remove_item(self, item):
        #if item in self.inventory:
            #print(f"You removed a {item} from your {self.name}.")
            #self.inventory.remove(item)
        #else:
            #print(f"Sorry their are no {item}s in your {Net}.")
    
    def add_item(self, item):
        if len(self.inventory) < self.capacity:
            print(f"You added a {item} to you inventory.")
            self.inventory.append(item)
        else:
            print(f"Sorry your inventory is already full.")
    
    
def playing():
    while True:
        options = ["Move", "Look at inventory"]
        print("What would you like to do?")
        for option in options:
            print(f" - {option}")
        choice_menu = (input("choice: ")).title
        if choice_menu == options[0]:
            player.movement()
        elif choice_menu == options[1]:
           player_inventory.view_inventory()
        else:
            print("sorry that was not a vaild choice")  

player = Player()
player_inventory = Inventory()
playing()