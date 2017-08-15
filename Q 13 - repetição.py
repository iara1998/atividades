#13. Criar um algoritmo que entre com vários números
#inteiros e positivos e imprima a média dos números
#múltiplos de 3. Considere a leitura de um número
#zero terminar.
y = []
soma = 0

x = int(input("Escreva números inteiros e positivos (0 encerra): "))

if x == 0:

	pass

else:
 
	while x != 0:
	 
	    if x == 0:
	 
	        break
	 
	    x = int(input())
	 
	    if x % 3 == 0:
	 
	        y.append(x)
	 
	for c in range(len(y)):
	 
	    soma += y[c]
	 
	print("A média dos números múltiplos de três (0 não considerado) é: %d" % (soma / int(len(y) - 1))) # Caso o programa não reconheça o zero como múltiplo dos números inteiros positivos (embora ele seja), o que eu suponho uma vez que o zero é utilizado para finalizar a sua execução
