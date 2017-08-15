#18. Imprimir todas as tabuadas de multiplicar de 1 até
#10.
def tabuada(n):

	for x in range(1,11):

		print("%d x %d = %d " % (n, x, n * x))

for x in range(1,11):

	tabuada(x)
    
