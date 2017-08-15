#20. Calcular a soma de n números inteiros lidos.
#Considere a leitura de um número zero como
#condição de parada.
y = []
soma = 0

print("Escreva números inteiros (0 encerra): ")

x = int(input())

if x == 0:

	pass

else:

	y.append(x)

	while x != 0:

		if x == 0:

			break

		x = int(input())

		y.append(x)

	for c in range(len(y)):

		soma += y[c]

	print("A soma dos números é %d. " % soma)
