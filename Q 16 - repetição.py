#16. Ler 200 números inteiros e imprimir quantos são
#pares e quantos são ímpares.
pares = 0
impares = 0
 
x = []
 
for c in range(200):
 
    x.append(int(input("X[%d] = " % c)))
 
for c in range(200):
 
    if x[c] % 2 == 0:
 
        pares += 1
 
    else:
 
        impares += 1
 
print("Pares = %d" % pares)
print("Ímpares = %d" % impares)
