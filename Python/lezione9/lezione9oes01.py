class Animal:
    def __init__(self, specie: str, age:int):
        self.specie: str = specie
        self.age: int = age
        return f'Animal(species={self.species}, age={self.age})'
    

class Person(Animal):
    def __init__(self, name: str, surname: str, cf: str, age: int):
        super().__init__("Homo Sapiens", self.age)
        self.name: str = name
        self.surname: str = surname
        self.cf: str = cf

    def speak(self) -> str:
        return f'Ciao mi chiamo {self.name} {self.surname} e ho {self.age} anni'

    def __str__(self) -> str:
        return f'{self.name.capitalize()} {self.surname.capitalize()} (cf={self.cf}'\
        + f', age{self.age})'\
        + f', specie={self.specie}'

p = Person(name="Giovanni", surname="Doge", cf="SSIUM", species="Homo Sapiens", age=88)

class Student:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age


class Cat:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Rabbit:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age