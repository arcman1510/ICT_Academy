class Person:
    # - name
    # - surname
    # - age
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age


lorenzo = Person("Lorenzo", "Maggi", 25)
print(f'Nome ={lorenzo.name}, Cognome {lorenzo.surname}, Età = {lorenzo.age}')
lorenzo.age = 22
print(f'Età = {lorenzo.age}')

danila = Person("Danila", "Uahatsou", 21)
print(f'Nome ={danila.name}, Cognome {danila.surname}, Età = {danila.age}')
danila.surname = "Rahatsou" #"Nono non Eue, la R di Roma Daje Roma"
print(f'Cognome = {danila.surname}')


name: str = input()
surname: str = input()
age: int = input()

person = Person(name, surname, age)
print(f'Persona con nome={person.name}, cognome={person.surname}, età={person.age}')


persons: list[Person] = [Person("Lorenzo", "Maggi", 22),
          Person("Oussama", "Hliwa", 21),
          Person("Bardh", "Prenkaj", 28)]
avg_age: float = 0
for person in persons:
    avg_age += person.age
avg_age /= len(persons)

