class Sala:

    def __init__(self, sala: str, film: str, posti_totali: int, posti_prenotati: int) -> None:
        self.sala: str = sala
        self.film: str = film
        self.poati_totali: int = posti_totali
        self.posti_prenotati: int = posti_prenotati
"""
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
"""