#9. Escreva	uma	função	que	recebe	e	retorne	o	valor	booleano	“verdadeiro”	caso	o	número	seja	múltiplo	de	5,	ou	
#“falso”,	caso	contrário.
def multiplo(z):

	return z % 5 == 0

try:

	z = int(input("Forneça um valor inteiro: "))

	print(multiplo(z))

except:

	print("Não foi fornecido um valor inteiro.")
