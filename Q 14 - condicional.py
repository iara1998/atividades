#14. Crie	uma	função	que	recebe	o	ano	de	nascimento	de	uma	pessoa	e	retorna	uma	mensagem	que	diga	se	ela	
#poderá	ou	não	votar	em	uma	eleição	para	prefeito,	não	é	necessário	considerar	o	mês	ou	o	dia	que	ela	nasceu.
def nascimento(ano):

	if 2020 - ano >= 16:

		return "Pode votar"

	else:

		return "Não pode  votar"

try:

	a = int(input("Escreva o valor correspondente ao teu ano de nascimento: "))

	print(nascimento(a))

except:

	print("Não foi fornecido um valor inteiro.")
