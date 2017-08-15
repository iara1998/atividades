#15. Entrar com um número e imprimir todos os seus
#divisores.
n = int(input("Digite um número inteiro: "))

print("Os divisores de %d são: " % n, end = "")

if n == 0:

	print("todos os números reais diferentes de zero.")

elif n > 0:

	for c in range(n,1,-1):

		if n % c == 0:

			print(c, end = ", ")

	print("1.")

elif n < 0:

	for c in range(n,0,1):

		if n % c == 0:

			print(c, end = ", ")

	for c in range(1,abs(n),1):

		if n % c == 0:

			print(c, end = ", ")

	print("%d." % abs(n))
