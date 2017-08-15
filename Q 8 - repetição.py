#08. Criar um algoritmo que leia um número que será o
#limite superior de um intervalo e o incremento
#(inc). Imprimir todos os números naturais no
#intervalo de zero até o limite superior. Suponha que
#o incremento é maior do que zero e o limite
#superior maior que o incremento.
l = int(input("Limite superior do intervalo: "))
inc = int(input("Incremento: "))

for a in range(0,l,inc):

	print(a)
