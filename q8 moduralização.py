#08. Recebe 2 números inteiros, retorne o quociente e o resto da divisão do 1º pelo 2º. Recebe um número inteiro e imprima de
#volta na tela
def divisao(x, y):

	q = x // y
	r = x % y

	return q, r

try:

	x, y = int(input("Forneça dois números inteiros: ")), int(input())

	q, r = divisao(x, y)

	print("O quociente da divisão de %d por %d é %d. O resto, %d." % (x, y, q, r))

except:

	print("Valores nvalidos.") 
