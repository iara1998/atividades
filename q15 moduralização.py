#15. Recebe um número no formato CDU e imprima na forma UDC. Exemplo: 123, sairá 321. O número deve ser armazenado em
#outra variável antes de ser impresso.
def veri(n):

	num = str(n)

	if len(num) == 3:

		return num

	else:

		return 0

n = int(input("Forneça um número de três algarismos: "))

if veri(n) == 0:

	print("Você não forneceu um número de três algarismos.")

else:

	print(veri(n)[::-1])
