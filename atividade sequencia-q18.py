#18. Construa um algoritmo para ler os coeficientes do
#polinômio P(x) = Ax4 + Bx3 + Cx2 + Dx + E. Depois, leia
#o valor de x, calcule e imprima o valor de P(x).
a = float(input("Forneça os valores dos coeficientes \"A\", \"B\", \"C\", \"D\" e do termo independente \"E\" do polinômio: "))
b = float(input())
c = float(input())
d = float(input())
e = float(input())

x = float(input("Forneça o valor correspondente à variável \"x\" do polinômio: "))

p = (a * pow(x, 4)) + (b * pow(x, 3)) + (c * pow(x, 2)) + (d * x) + e

print("O valor de P(x) é", p, end = ".\n")
