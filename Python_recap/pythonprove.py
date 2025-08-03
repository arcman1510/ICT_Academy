#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, 
#represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 
#Versione con input

famous_person: str = input("Inserisci il nome della persona famosa: ")
quote: str = input("Inserisci la citazione della persona: ")

message: str = f'{famous_person} once said, "{quote}"'
print(message)