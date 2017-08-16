#02. Recebe um valor em real (R$), retorna 70% deste valor.
try:

	def calcPorcent(v):

		return v * 0.7

	x = float(input("Forneça o valor em real (R$): "))


	print("70%c de %f é %f." % ("%", x, calcPorcent(x)))

except:

	print("Você não forneceu um valor real.")
