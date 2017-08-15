#17. Ler o número de termos da série (n) e imprimir o
#valor de H, sendo:
h = 1
 
try:
 
    n = int(input("n = "))
 
    for c in range(2,n + 1):
 
        h += 1 / c
 
    print("H = %f" % h)
 
except:
 
    print("Não foi fornecido um valor inteiro.")
