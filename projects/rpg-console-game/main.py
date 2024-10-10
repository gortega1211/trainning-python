from room import Room
from character import Enemy, Friend
from item import Item
from rpginfo import RPGInfo

"""
Challenge 4
Use a class variable to allow the player to win the game only after they have defeated a specific number of enemies, rather than winning
it the instant they defeat a single enemy.

"""

def run():
    spooky_castle = RPGInfo("The Spooky Castle")
    spooky_castle.welcome()
    RPGInfo.info()

    RPGInfo.author = "Gustavo Ortega"
    RPGInfo.credits()

    backpack = []

    knife = Item("Knife")
    knife.set_description("A very sharp knife.")

    kitchen = Room("Kitchen")
    kitchen.set_description("A dank and dirty room buzzing with flies.")
    kitchen.set_item(knife)
    
    dining_hall = Room("Dinning Hall")
    dining_hall.set_description("A large room with ornate golden decorations on each wall.")

    ballroom = Room("Ballroom")
    ballroom.set_description("A vast room with  a shiny wooden floor. Huge candlesticks guard the entrance.")

    kitchen.link_room('south', dining_hall)
    dining_hall.link_room('north', kitchen)
    dining_hall.link_room('west', ballroom)
    ballroom.link_room('east', dining_hall)

    print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

    dave = Enemy("Dave", "A smelly zombie")
    dave.set_conversation("Brrlgrh... rgrhl... brains...")
    dave.set_weakness("cheese")
    dining_hall.set_character(dave)

    catrina = Friend("Catrina", "A friendly skeleton")
    catrina.set_conversation("Why hello there.")
    ballroom.set_character(catrina)

    current_room = kitchen
    dead = False
    while dead == False:
        current_item = current_room.get_item()
        current_room.get_details()
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()
        command = input(" > ")
        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)

        elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()                
        
        elif command == "fight":
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                print("What will you fight with?")
                fight_with = input()
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        print("Hooray, you wont the fight!")
                        current_room.set_character(None)
                        if Enemy.enemies_to_defeat == 0:
                            print("Congratulations, you have vanquished the enemy horde!")
                            dead = True
                    else:
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
                
            else:
                print("There is no one here to fight with")

        elif command == "hug":
            if inhabitant is not None:
                if isinstance(inhabitant, Enemy):
                    print("I wouldn't do that if I were you...")
                else:
                    inhabitant.hug()
            else:
                print("there is no one here to hug :(")

        elif command == "search":
            if current_item is not None:
                print(current_item.describe())

        elif command == "take":
            if current_item is not None:
                print("You put the " + current_item.get_name() + " in your backpack")
                backpack.append(current_item.get_name())
                current_room.set_item(None)

if __name__ == "__main__":
    run()