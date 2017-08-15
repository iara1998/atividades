#13. Escreva	uma	função	que	retorne	“verdadeiro”	se	um	número	recebido	for	par	e	divisível	por	3.
def inte(c):

	return c % 2 == 0 and c % 3 == 0

try:

	c = int(input("Escreva um valor inteiro: "))

	print(inte(c))

except:

	print("Não foi fornecido um valor inteiro.")
