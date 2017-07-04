#12. Recebe quatro números e imprima a média ponderada, sabendo-se que os pesos são respectivamente 1, 2, 3 e 4.
a = int(input("Digite o primeiro numero"))
b = int(input("Digite o segundo numero"))
c = int(input("Digite o terceiro numero"))
d = int(input("Digite o quarto numero"))
def ponderada(a, b, c, d):
    x = (a*1+b*2+c*3+d*4)/10
    return(x)

print (" A media ponderada e:",ponderada(a, b, c, d))
