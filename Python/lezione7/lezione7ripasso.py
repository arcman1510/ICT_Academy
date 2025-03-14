"""
Scrivi una funzione che ruota gli elementi 
di una lista verso sinistra di un numero specificato k 
di posizioni. La rotazione verso sinistra significa che 
ciascun elemento della lista viene spostato a sinistra 
di una posizione e l'elemento iniziale viene spostato 
alla fine della lista. Per la rotazione utilizzare 
lo slicing e gestire il caso in cui il numero specificato 
di posizioni sia maggiore della lunghezza della lista.

Test 	
print(rotate_left([1, 2, 3, 4, 5], 2))

	
Result
[3, 4, 5, 1, 2]
"""


def rotate_left(elements: list, k: int) -> list:
    # Loop through the range of n positions to rotate
    for i in range(k):
        # Remove the last element of the list and insert it at the beginning
        elements.insert(0, elements.pop())
    # Return the rotated list
    return elements
 
# Example usage:
print(rotate_left([1, 2, 3, 4, 5], 2))