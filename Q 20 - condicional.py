#20. O	índice	de	massa	corporal	(IMC)	é	uma	medida	internacional	usada	para	calcular	se	uma	pessoa	está	no	peso	
#ideal. O	IMC	é	determinado	pela	divisão	da	massa	do	indivíduo	pelo	quadrado	de	sua	altura,	em	que	a	massa	
#está	em	quilogramas	e	a	altura	em	metros. Faça	uma	função	que	retorna	o	IMC	de	uma	pessoa,	e	depois,	exiba	
#uma	das	seguintes	mensagens:
def imc(massa, altura):

	return massa / (altura ** 2)

massa, altura = float(input("Forneça os valores reais correspondentes à massa (em kg) e à altura (em m): ")), float(input())

if massa > 0 and altura > 0:

	imc = imc(massa, altura)

	if imc < 18.5:

		classificacao = "Abaixo do peso"

	elif imc < 25 and imc >= 18.5:

		classificacao = "Peso normal"

	elif imc < 30 and imc >= 25:

		classificacao = "Sobrepeso"

	elif imc < 35 and imc >= 30:

		classificacao = "Obeso leve"

	elif imc < 40 and imc >= 35:

		classificacao = "Obeso moderado"

	elif imc >= 40:

		classificacao = "Obeso mórbido"

	print("IMC = %.3f" % imc)
	print("%s" % classificacao)

else:

	print("Valor(es) inválido(s).")
