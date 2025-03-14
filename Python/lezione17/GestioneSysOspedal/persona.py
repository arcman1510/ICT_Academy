class Persona:

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: float = age
        
        for first_name in self:
            if first_name is True:
                print("Benvenuto")
            else:
                print("Nome non valido")
        for last_name in self:
            if first_name is True:
                print("Benvenuto")
            else:
                print("Nome non valido")

        