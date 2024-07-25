class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


alice = Person("ALice W.", 45)
bob = Person("Bob M.", 36)

print(f'Nome ={alice.name}, Età = {alice.age}')
print(f'Nome ={bob.name}, Età = {bob.age}')


if bob.age > alice.age:
    print(bob.age)
else:
    print(alice.age)

lorenza = Person("Lorenza Maggi", 33)
lollito = Person("Lollito Chicano", 31)
doge = Person("Giovanni Doge", 88)
paddy = Person("Andrea Paddington", 21)
mlis = Person("Marco LODATEILSOLE", 18)
gimdad = Person("Gimmi SuperDaddy", 19)

pippol:list[Person] = [alice, bob, lorenza, lollito, \
                       doge, paddy, mlis, gimdad]

pupo:None = None
for i in pippol:
    if pupo == None:
        pupo = i.age
    else:
        if pupo > i.age:
            pupo = i.age
    if pupo == mlis.age:
        print(mlis.name)
        print("HAI MAI LODATO IL SOLE?!?1?1?!")

print(pupo)


