class Food:

    def __init__(self, name: str, price: float, description: str = None):
        self.name = name
        self.price = price
        self.description = description



class Menu:

    def __init__(self, foods: list[Food] = []):
        self.foods: list[Food] = foods

    def add_food(self, food: Food):
        self.foods.append(food)

    def remove_food(self, food: Food):
        if food in self.foods:
            self.foods.remove(food)

    def __str__(self) -> str:
        repr: str = ""
        for food in self.foods:
            repr += "\n" + food.__str__()
        return repr[1:]
    
carbonara = Food(name= "Carbonara", price=15.5)
cacio_e_pepe = Food(name="Cacio e Pepe", price=9.8)

menu = Menu()