#09. Criar um algoritmo que calcule a soma dos
#números pares entre 25 e 200.
soma = 0
x = []
 
for b in range(24,200,2):
 
	x.append(b)
 
for b in range(0,len(x)):
 
	soma += b
 
print("A soma dos números pares  é %d." % soma)
