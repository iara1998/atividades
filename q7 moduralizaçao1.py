#Recebe 2 números, retorne a divisão da soma pela subtração dos números lidos.

def div_som(x, y):
    f = (x+y)/(x-y)
    return (f)
x = int(input("Digite o primeiro valor:"))
y = int(input("Digite o segundo valor:"))
f = div_som(x, y)
print ("A divisao e:",f)
       
