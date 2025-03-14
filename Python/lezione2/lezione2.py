#Manuel Archer
#18/04/2024

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

#2-8. File Extensions: 
#Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename: str = 'python_notes.txt'
print(filename)
print(filename.removesuffix(".txt"))
print("")


"""
3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.
"""
immaginaryfriendslist = ["Tizio", "Caio", "Sempronio", "Ronaldo", "Zanetti"]

"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
 print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
"""