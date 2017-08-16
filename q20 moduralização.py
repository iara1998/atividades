#20. Um algoritmo para realizar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o número de notas
#de cada valor que deve ser disponibilizado para o cliente que realizou o saque. Um possível critério seria o da "distribuição
#ótima" no sentido de que as notas de menor valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo,
#se a máquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo
#deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que
#receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.
def caixa(q):

	cin = q // 50
	dez = (q % 50) // 10
	cinc = ((q % 50) % 10) // 5
	um = q - ((cin * 50) + (dez * 10) + (cinc * 5))

	return cin, dez, cinc, um

try:

	q = int(input("Escreva o valor correspondente à quantia solicitada: "))

	print("Notas de R$ 50,00: %d\nNotas de R$ 10,00: %d\nNotas de R$ 5,00: %d\nNotas de R$ 1,00: %d" % caixa(q))

except:

	print(" não forneceu um valor inteiro.")
