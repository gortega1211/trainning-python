class Room:

    number_of_rooms = 0
    
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

        Room.number_of_rooms = Room.number_of_rooms + 1

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def set_description(self, room_description):
        self.description = room_description
    
    def get_description(self):
        return self.description

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def describe(self):
        print(self.description)

    def link_room(self, direction, room_to_link):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print("\n" + self.name)
        print("-" * 10)
        self.describe()
        for direction, link_room in self.linked_rooms.items():
            print("The " + link_room.get_name() + " is the " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("\nYou can't go that way.")
            return self
