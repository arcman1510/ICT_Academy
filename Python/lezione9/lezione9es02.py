class Room:

    def __init__(self, id: str, floor: int, seats: int, area: float):
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: float = 2 * self.seats

    def __str__(self) -> str:
        return f'Room(id={self.id}, floor={self.floor}, seats={self.seats})'

class Building:

    def __init__(self, name: str, address: str, num_floors: int, rooms: list[Room] =  []) -> None:
        self.name: str = name
        self.address: str = address
        self.num_floors: int = num_floors
        self.rooms: list[Room] = rooms

    def get_num_floors(self) -> int:
        return self.num_floors
    
    def add_room(self, room: Room):
        if room not in self.rooms\
        and room.get_floor() <= self.get_num_floors():
            self.rooms.append(room)
    
    def area(self) -> float:
        sum_area: float = 0
        for room in self.rooms:
            sum_area += room.get_area()
        return sum_area
    
    def __str__(self) -> str:
        s: str = f'{self.name} @ {self.address}\n'
        s+= "With Rooms: \n"
        for room in self.get_rooms():
            s += room.__str__() + "\n"
        return s + self.area()

class Person:

    def __init__(self, cf: str, name:str, surname: str, age: int):
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age

   
        

#class Group:

    #def __init__(self, name: str, limit: int):
    
#Test di unità, il codice funziona nonostante ci siano anomalie all'interno del codice

class BelloMio:

    def __init__(self, fregati):
        self.fregati = fregati

smi = Building(name="SMI", address="Via Sierra Nevada 60", num_floors=5)
armellini = Building(name="ITIS", address="Basilica San Paolo", num_floors=3)

smi.add_room(Room(id="666", floors=3, seats=32))

