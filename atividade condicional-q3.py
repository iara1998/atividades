#3. Faça	uma	função	que	recebe	dois	números	por	parâmetro	e	retorna	o	maior
def maior(a, b):

	if a > b:

		return a

	else:

		return b

try:

	a, b = float(input("Coloque dois números reais: ")), float(input())

	if a != b:

		print("O maior valor é %f.\n" % maior(a, b))

	else:

		print("Os valores são iguais.")

except:

	print("Não foram fornecidos valores reais.")
