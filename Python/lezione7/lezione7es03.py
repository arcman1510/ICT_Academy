class Animal:

    def __init__(self, name: str, legs: int):
        self.name: str = name
        self.legs: str = legs

    def set_legs(self, new_legs: int):
        if new_legs >= 0:
            self.legs
        else:
            self.legs = 0

    def get_legs(self) -> int:
            return self.legs
    
    def __str__(self) -> str:
        return f'Name: {self.name}, Legs: {self.legs}'
    
    """
    spider = Animal("Spider", 8)
    rat = Animal("Rat.", 3)
    print(f'Nome ={spider.name},  Legs = {spider.legs}')
    print(f'Nome ={rat.name},  Legs = {rat.legs}')
       rat.legs = 4
    print(f'Legs = {rat.legs}')
    """