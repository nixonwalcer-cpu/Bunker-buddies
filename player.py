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
    
    
def playing():
    while True:
        player.movement()   

player = Player()
playing()