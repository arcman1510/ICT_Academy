from ITS.course.course import Course
from ITS.group import Group
from ITS.people.student import Student

class Room:
    
    def __init__(self, id: str, floor: int, seats: int):
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: float = 2 * self.seats
        
    def get_floor(self) -> int:
        return self.floor
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_id(self) -> str:
        return self.id
    
    def get_area(self) -> float:
        return self.area
        
    def __str__(self) -> str:
        return f'Room(id={self.get_id()}, floor={self.get_floor()}, seats={self.get_seats()})'

class Building:
    
    def __init__(self, name: str, address: str, floors: tuple[int, int]):
        self.name: str = name
        self.address: str = address
        self.floors: int = floors
        self.rooms: list[Room] = []
        
    def get_floors(self) -> tuple[int, int]:
        return self.floors
    
    def get_rooms(self) -> list[Room]:
        return self.rooms
        
    def add_room(self, room: Room):
        floors = self.get_floors()
        if room and isinstance(room, Room) and room not in self.rooms\
            and floors[0] <= room.get_floor() <= floors[1]:
            self.rooms.append(room)
            
    def area(self) -> float:
        sum_area: float = 0
        for room in self.rooms:
            sum_area += room.get_area()
        return sum_area
        
    def __str__(self) -> str:
        s: str = f'{self.name} @ {self.address}\n'
        s += "With Rooms:\n"
        for room in self.get_rooms():
            s += room.__str__() + "\n"
        return s + f'Area = {self.area()}m2'
    

        

    
                

        
    
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=[-2,3])
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=[0,4])

smi.add_room(Room(id="666", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))
smi.add_room(Room(id="111", floor=-1, seats=32))

fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="cloud", limit=10)
cyber = Group(name="cyber", limit=10)

course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="1234", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="1234", name="Toni", surname="Mancini", age=46))
print(f'Studenti in fullstack: {len(course.groups[0].students)}')
print(f'Studenti in cloud: {len(course.groups[1].students)}')
print(f'Studenti in cyber: {len(course.groups[2].students)}')