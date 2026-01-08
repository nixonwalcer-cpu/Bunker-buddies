#ONLY FOR NIXON

class Room
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.name.title()

    
    
map = [[bathroom, boiler],
       [entrence, kitchen],
       [hallway, bedroom]]
 




boiler_room = room ("boiler room", "the boiler is broken and you need to," \
                    +"fix it because its getting really cold........"),
kitchen = room ("kitchen", "the kitchen has a hole in the ceiling ......."),
bedroom = room ("bedroom", "the bedroom wall has a crack in  it.......")
hallway = room ("hallway", "the hallway has a leaking pipe......" )
bathroom = room ("bathroom", "the toilet is broken........")
entrence = room ("entrence","the entrence is " )


print(map[0][1])





#if __name__ == "__main__":
    #This code will not run during the game.
    #This code is for just testing the bunker features.
    print("World")