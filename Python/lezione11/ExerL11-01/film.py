class Film:
       def __init__(self, id: str, titolo: str, duratam: int):
        self.id: str = id
        self.titolo: str = titolo
        self.duratam: int = duratam

        def __str__(self) -> str:
            return f'Id Film(id={self.id}, titolo ={self.titolo}, durata in minuti ={self.seats})'
    