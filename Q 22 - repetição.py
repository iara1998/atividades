#22. Dados dois números inteiros positivos, determinar
#o máximo divisor comum entre eles usando o
#algoritmo de Euclides.
def euclides(a, b):
    
    if b == 0:
        
        return a
    
    else:
        
        return euclides(b, a % b)
 
a, b = int(input("Forneça dois números inteiros positivos: ")), int(input())

if a > 0 and b > 0:


	print("O MDC entre %d e %d é %d." % (a, b, euclides(a, b)))



else:

	print("Erro: é preciso que dois números inteiros e positivos sejam fornecidos.")
