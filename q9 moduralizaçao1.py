#09. Recebe um número inteiro e imprima na tela seu antecessor e o seu sucessor.
def ant_suc( x ):  
    b = x-1
    c = x+1
    return (b ,c)
x = int(input("Digite um valor:"))
b = ant_suc(x)
print ("O antecessor e sucessor do numero e respectivamente",b)
