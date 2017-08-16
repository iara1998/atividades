#14. Recebe um número inteiro de 3 dígitos e mostre na tela o dígito da casa das dezenas
def dezenas(n):

	num = str(n)

	if len(num) == 3:

		c = n // 100 
		d = (n - (c * 100)) // 10
		
		return d

	else:

		return 71

n = int(input("Escreva um número inteiro com três algarismos: "))

if dezenas(n) == 71:

	print("Você não forneceu um número com três algarismos.")

else:

	print("O algarismo das dezenas é %d." % (dezenas(n)))
