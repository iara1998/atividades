#17. Em época de pouco dinheiro os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Recebe o valor de
#um produto e o percentual de desconto concedido e imprima o valor do produto com desconto.
def desc(pr, p):

	return pr - (pr * (p / 100))

try:

	pr, p = float(input("Forneça o valor correspondente ao preço do produto e o valor correspondente ao percentual de desconto: ")), float(input())

	print("O preço do produto é %f." % (desc(pr, p)))

except:

	print(" não forneceu valores reais.")
