#4. Faça	uma	função	que	recebe	três	números	por	parâmetro	e	imprime	na	tela	em	ordem	crescente.
def rece(x, y, z):

	numeros = [x, y, z]

	numeros.sort()

	print("Em ordem crescente: %f, %f, %f." % (numeros[0], numeros[1], numeros[2])).rstrip('.').rstrip('0')

try:

	x, y, z = float(input("Forneça três números: ")), float(input()), float(input())

	rece(x, y, z)

except:

	print("Não foram fornecidos valores reais.")
