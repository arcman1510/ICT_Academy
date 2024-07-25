"""
3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.
"""
names = ["Tizio", "Caio", "Sempronio"]

print(names[0])
print(names[1])
print(names[2])


"""
3-2. Greetings: Start with the list you used in Exercise 3-1, 
but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be personalized with the person’s name.
"""

print("Hello, my good friend {}".format(names[0]))
print("Hello, my good friend {}".format(names[1]))
print("Hello, my good friend {}".format(names[2]))

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
and make a list that stores several examples. Use your list to print a series of statements about these items, 
such as “I would like to own a Honda motorcycle.”
"""

fav_transpo = ['car', "airplane"]

print("I go to work by {}".format(fav_transpo[0]))
print("I travel overseas by taking a/an {}".format(fav_transpo[1]))

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner.
"""

guests = ['Ronaldo', 'Zanetti', 'Lukaku']

name = guests[0].title()
print(name + ", I would like to invite you to dinner.")

name = guests[1].title()
print(name + ", I would like to invite you to dinner.")

name = guests[2].title()
print(name + ", I would like to invite you to dinner.")


"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# Lukaku can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'Lautaro')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", I would like to invite you to dinner.")

name = guests[1].title()
print(name + ", I would like to invite you to dinner.")

name = guests[2].title()
print(name + ", I would like to invite you to dinner.")


"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. 
Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""
print("\nWe've got a bigger table!")
guests.insert(0, 'Handanovic')
guests.insert(2, 'Barella')
guests.append('Milito')

name = guests[0].title()
print(name + ", I would like to invite you to dinner.")

name = guests[1].title()
print(name + ", I would like to invite you to dinner.")

name = guests[2].title()
print(name + ", I would like to invite you to dinner.")

name = guests[3].title()
print(name + ", I would like to invite you to dinner.")

name = guests[4].title()
print(name + ", I would like to invite you to dinner.")

name = guests[5].title()
print(name + ", I would like to invite you to dinner.")

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, 
and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.
"""

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")


# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)

"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
"""
locations = ['Olso', 'Copenhagen', 'Madagascar', 'Luknow', 'Tokyo']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.
"""

invitations = ["Ronaldo", "Milito", "Zanetti"]
count_invitations = len(invitations)

print("{} people will come to my dinner party".format(count_invitations))

"""

3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

x=["cat",2.5,500,True]
print(x)
x[1]="dog" # changing first element of x from 2.5 to dog
print(x)

bike=["honda","yamaha","suzuki"]
del bike[1] #deleting the value at index 1 from x
print(bike)

x=["cat",2.5,500,True]
x.insert(1,"dog")#its insert the element in given position
print(x)

x.append(False)#it will append the element at last
print(x)

y=x.pop(2)#it will pop that element out at given index and remove from that list If no index is specified , list.pop() removes the last item in the list
print(y+1)#you can also play with that pop out no
print("pop",x)

x.remove(False)#it will remove the given elment from the list
print(x)

list_one = [1, 2, 3, 4, 5, 6, 7]  # This is the first list
list_two = [10, 12, 14]           # This is the second list
list_one.extend(list_two)         # Extend list_one by appending all items of list_two
print(list_one)

my_list = [2, 3, 5, 7, 11, 13] # Create a list
my_list.clear()                # Remove all the items from the list
print(my_list) 

my_list = ["Python", "is", "awesome", "Java", "is", "Alright"]# Create a list
my_index = my_list.index("is")                                # Return the index of the first "is"
print("The item was first found at index:", my_index)

my_list = ["mew", "mew", "kitten", "mew", "mew"]                  # Create a list
my_count = my_list.count("mew")                                   # Return the number of times "mew" appears
print("The number of times the item appeared was:", my_count)

my_list = ["zero", "one", "two", "three", "four", "five"]        # Create a list
my_list.reverse()                                                # Reverse the items of the list in place
print("Reversed list looks like:", my_list)

my_list.sort(reverse=True)                             #it will sort list in descending order
print(my_list)

my_list.sort()                             #it will sort list in ascending order
print(my_list)

original_list = ["zero", "one", "two", "three"]        # Create a list
copied_list = original_list.copy()                     # Copy the original list and return it.        
print("Copied list looks like:", copied_list)

my_list = ['two', 5, ['one', 2]]
print(len(my_list))


my_list = [5, 3, 6, 1, 2, 4, 7]                  # Create a list
sorted(my_list, reverse=True)             # Sorted the items of the list in sort the item permenantlyorder
print("Sorted list looks like:", my_list)

my_list=['a','g','d','f','t','x','l']
my_list.sort()
print(my_list)