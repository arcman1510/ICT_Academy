#let's try to define a funciton named "subtract" ourselvese
#it should take 2 parameters
#inside the funciton, it should subtract the to
#then, return the result
#after you defined it, call the funciton with some arguments

def subtract(a, b):
    res = a - b
    return res

myresult = subtract(4, 1)
print(myresult)


print("")

def check_value(num:int):
    if num > 5:
        print("num is greater than 5")
    elif num < 5:
        print("num is less than 5")
    else:
        print("num is equal to 5")
check_value(10)

print("")

def check_length(s: str):
    if len(s) <10:
        print(f'{s} è più piccolo di 10 chars')
    elif len(s) > 10:
        print(f'{s} è più grande di 10 chars')
    else:
        print(f'{s} è uguale a 10 chars')

def print_numbers(num_list):
    for element in num_list:
        print(element)
 

def check_each(s):
    if len(s) < 10:
        print(f'{s} è più piccolo di 10 chars')
    elif len(s) > 10:
        print(f'{s} è più grande di 10 chars')
    else:
        print(f'{s} è uguale a 10 chars')