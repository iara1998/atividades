#5. Crie	uma	função	que	recebe	um	número	por	parâmetro	e	retorna	o	valor	booleano	verdadeiro	se	o	número	
#for	par.
def num(x):

	return x % 2 == 0

try:

	x = int(input("Forneça um número inteiro: "))

	print(num(x))

except:

	print("Numero invalido.")
