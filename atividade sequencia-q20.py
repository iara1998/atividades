#20. Faça um algoritmo que efetue a apresentação do valor da
#conversão em real de um número lido em dólar. O
#programa lerá o calor da cotação do dólar e a quantidade
#de dólares com o usuário, para apresentar o valor em
#moeda brasileira.
c = float(input("Forneça o valor correspondente à cotação do dólar: "))
d = float(input("Forneça o valor correspondente à quantidade de dólares: "))

print("O valor em reais é", d * c, end = ".\n")
