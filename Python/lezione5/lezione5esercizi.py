"""
Q1
La funzione dovrebbe determinare se un elemento è presente in una lista.
Un errore nell'implementazione porta a risultati inaspettati.
 
TROVA L'ERRORE E CORREGGI IL CODICE



def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
        return False
"""   
"""
def find_element(lst: list[int], n: int) -> bool:
    i=0
    for value in lst:
        if value == n:
            return True
        i += 1
    return False
print(find_element([1, 2, 3, 4, 5], 5))
"""

"""
Q2
Scrivi una funzione che calcola la media 
di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.

For example:
Test 
print(rounded_average([1, 1, 2, 2]))
	
Result
2
"""
"""
def rounded_average(numbers: list[int]) -> int:
    average:int = round(sum(numbers)/len(numbers))
    return average
print(rounded_average([1, 1, 2, 2]))
"""

"""
Q3

"""
"""
def rotate_left(elements: list, k: int) -> list:
    # Loop through the range of n positions to rotate
    for i in range(k):
        # Remove the last element of the list and insert it at the beginning
        elements.insert(0, elements.pop())
    # Return the rotated list
    return elements

"""





"""
Q4
La funzione dovrebbe calcolare 
la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.
"""
"""
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return len(numbers) / (sum(numbers) -1)
    else:
        return sum(numbers) / len(numbers)
    
print(calculate_average([]))
"""


"""
Q6
Scrivi una funzione che ritorna il valore massimo, 
minimo e la media di una lista di numeri interi.
"""
"""
import statistics
def list_statistics(numbers: list[int]) -> ... :
    # cancella ... e definisci il tipo del dato di ritorno, successivamente cancella pass e scrivi il tuo codice
    i: int
    j: int
    k: int
    for i in numbers:
        maximum = max(numbers)
        return maximum
    for j in numbers:
        minimun = min(numbers)
        return minimun
    for k in numbers:
        sum = sum(numbers)
        length = len(numbers)
        average = sum/length
        return average


print(list_statistics([1, 2, 3, 4, 5]))
"""

def is_magic_number(num: int) -> bool:
    for num in range(10000):
        if '7' in str(num):
            return True
        else:
            return False
print(is_magic_number(70))
print(is_magic_number(123))