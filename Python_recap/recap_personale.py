mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)
    
print('')
print('')
    
for num in mylist:
    print('hello')

print('')
print('')

    
for num in mylist:
    #controllare numeri pari. % (modulo) calcola
    # il resto dei numeri
    # quindi 4 % 2 lascia il resto di 0
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

print('')
print('')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    print(list_sum)
    
print('')
print('') 
 
mystring = 'Hello World'   
#posso anche scrivere  for letter in 'Hello World'  
for letter in mystring:
    print(letter)

print('')
print('')

#tupla
tup = (1,2,3)

for item in tup:
    print(item)
    
mylist1 = [(1,2),(3,4),(5,6),(7,8)]

#lunghezza della lista
len(mylist1)

#spacchettamento di una tupla
for item in mylist1:
    print(item)
    
for a,b in mylist1:
    print(a)
    print(b)
    
mylist1 = [(1,2,3),(5,6,7),(8,9,10)]