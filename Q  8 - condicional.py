#8. Crie	uma	função	que	recebe	um	número	inteiro	e	retorne	a	mensagem	positivo,	negativo	ou	igual	a	zero,	de	
#acordo	com	o	valor	recebido.
def inteiro(f):

	if f == 0:

		return "igual a zero"

	elif f < 0:

		return "negativo"

	elif f > 0:

		return "positivo"

try:

	f = int(input("Forneça um valor inteiro: "))

	print("O número %d é %s." % (f, inteiro(f)))

except:

	print("Não foi fornecido um valor inteiro.")
