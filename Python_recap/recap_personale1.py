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