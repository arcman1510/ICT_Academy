#while loop continua ad eseguire un blocco di codice
#finché una condizione/variabile è vera

#possiamo abbinare il while con else
#while "condizione booleana"
#      fai qualcosa
#else:
#   fai una cosa diversa

x = 0

while x <= 5:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print(f'X is not less than 5')
    




print('')
print('')
 



#----------------------

mylist = [1,2,3]

print('da 3 a 10')

for num in range(3,10):
    print(num)
    
print('')
print('')
print('da 0 a 10 intervallo di 2')
    
for num in range(0,11,2):
    print(num)
    
    
print('')
print('')
    
#range è un generatore, un tipo speciale di funzione (non può rimanere solo), specifica i limiti
#primo numero = inizio
#secondo numero = fine (non incluso quel numero)
#terzo numero = a intervalli di n

index_count = 0

#for letter in 'abcde':
#    print('At index {} the letter is {}'.format(index_count,letter))
#    index_count += 1

#'At index {} the letter is {}'
#→ è la stringa modello, con due “buchi” {} da riempire.
#.format(index_count, letter)
#→ dice: “Riempimi il primo buco col valore di index_count, e il secondo con letter.”

    
for letter in 'abcde':
    print(f'At index {index_count} the letter is {letter}') 
    index_count += 1

