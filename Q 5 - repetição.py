#05. Faça um programa que peça uma nota, entre zero e
#dez. Mostre uma mensagem caso o valor seja
#inválido e continue pedindo até que o usuário
#informe um valor válido.
try:

	nota = float(input("Forneça uma nota (entre 0 e 10): "))

except:

	print("Não foi fornecido um valor real.")

	nota = 1

while nota < 0 or nota > 10:

	try:

		nota = float(input(" Forneça uma nota válida (entre 0 e 10): "))

	except:

		print("Não foi fornecido um valor real.")
