#14. Escreva um algoritmo que leia um conjunto de 100
#números inteiros positivos e determine o maior
#deles.
a = []

for c in range(100):

	a.append(int(input("A[%d] = " % c)))

a.sort()

print("\n%d" % a[99]) 
