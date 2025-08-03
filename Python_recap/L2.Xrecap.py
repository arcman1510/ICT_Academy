print("Hello World")

#2-3. Personal Message: Use a variable to represent a person’s name, and 
#print a message to that person. Your message should be simple, 
#such as, “Hello Eric, would you like to learn some Python today?”




# Questa variabile contiene il nome
name: str = "Mario"
print(f"Ciao {name}, etc....")

print("")

# Questa variabile contiene il messaggio
name: str = "Mario"
message: str = (f"Ciao {name} , ti va di imparare un po di python insieme?")

print(message)


print("")

#
#2-4. Name Cases: Use a variable to represent a person’s name 
#then print that person’s name in lowercase, uppercase, and title case.

#Questa è una variabile che contiene il nome di una persona
name: str = "Mario"


#Questa è una variabile che contiene il nome minuscolo
name_lower: str = name.lower()


#Questa è una variabile che contiene il nome maiuscolo
name_upper: str = name.upper()

print(f"{name}, {name_upper} , {name_lower}")
print("")

print(f"Ecco come appare il nome del mio Fratellino nei tre stili principali:")

fratellino: str = "Kai Leoni"

print(fratellino.lower())
print(fratellino.upper())
print(fratellino.title())


print(f"Ecco come appare il nome del mio Fratellone nei tre stili principali:")

fratellone: str = "Manuel Archer"

print(fratellone.lower())
print(fratellone.upper())
print(fratellone.title())


#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following, including the quotation marks: 
#Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print("Albert Einstein once said, “A person who never made a mistake never tried anything new.” ")
print("")

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, 
#represent the famous person’s name using a variable called famous_person. 
#Then compose your message and represent it with a new variable called message. Print your message. 

famous_person: str = "Albert Einstein"
message: str = ("once said, 'A person who never made a mistake never tried anything new.'")
print(famous_person, message)
print("")

famous_person: str = "Albert Einstein"
quote: str = '"A person who never made a mistake never tried anything new."'
message: str = f"{famous_person} once said, {quote}"
print(message)


famous_person: str = "Albert Einstein"
quote: str = '"A person who never made a mistake never tried anything new."'
message: str = f"{famous_person} once said, {quote}"

print("Il silenzio della sera si posa piano sulle cose...")
print("Io e te seduti in terrazza, senza bisogno di troppe parole.")
print("Poi guardo le stelle, ti sorrido e dico:")
print(message)


famous_person: str = input("Inserisci il nome della persona famosa: ")
quote: str = input("Inserisci la citazione della persona: ")

message: str = f'{famous_person} once said, "{quote}"'
print(message)


#2-8. File Extensions: 
#Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename: str = 'python_notes.txt'
print(filename)
print(filename.removesuffix(".txt"))
print("")