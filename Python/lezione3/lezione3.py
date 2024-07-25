lista = ["manamana", "102938", "plis", "wut"]

x = max(lista)
print(lista)

y = min(lista)
print(lista)


print("")
#definiamo le variabile che useremo per calcolare l'area
#scrivo la riga di stampa dove chiamo le variabili x ed y
# il return mi serve per restituirmi le due variabili moltiplicate
#   l'unico modo per "comunicare col mondo esterno"
# è se eseguo il "print"
# posso assegnare un'altra variabile out che equivale a questa molt.
#
def area(x:float,y:float) -> float:
    print (f' x={x}, y={y}')
    #return x * y
    out = x * y
    print(f"l'area è {out}")


print("")
#questo paragrafo mi stampa non solo nuove stringhe
#ma avendo i numeri assegnati ai numeri
#posso eseguire l'operazione
print("bella")
x,y = (2, 3)
#print(area(x,y))
out = area(x, y)
print(out)

print("")

#
#
#
""""
def sum(l: list[float]) -> float:
    somma = 0
    i = 0
    while i < len(l):
"""

#sorted() restituisce una nuova lista ordinata
# dagli elementi di un iterabile
mylist = [5, 2, 9, 1]
sorted_list = sorted(mylist)
print(sorted_list)

l = [8, -1, 29, 0, 10.5]
# l1 = sorted(l)
# l1 = sorted(l, reverse true)
# l1 = sorted(l)[::-1]
# l1 = [-1,0,0,8,10.5,29]
# l1 = l1[::-1] ->
#
l1 = list(set(l))

