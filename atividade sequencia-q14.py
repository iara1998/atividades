#14. Faça um algoritmo que leia dois inteiros A e B, e crie um
#algoritmo para trocar os valores dessas variáveis.
c = 0
d = 0

a = int(input("Forneça dois valores inteiros para \"a\" e \"b\", respectivamente: "))
b = int(input())

c = a
d = b
b = c
a = d

print("O valor de \"a\" é", a, "e o de \"b\" é", b, end = ".\n")
