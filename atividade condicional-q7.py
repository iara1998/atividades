#7. Crie	uma	 função	que	recebe	o	nome	e	o	sexo	de	uma	pessoa,	e	retorne a	mensagem	“Ilmo	Sr.”,	caso	seja	
#informado	o	sexo	masculino,	ou	“Ilma	Sra.”,	caso	seja	informado	o	sexo	feminino.	Retorne	junto	com	cada	
#mensagem	de	saudação	o	nome	que	foi	informado.
def tratar(nome, sexo):

	if sexo.lower() == "masculino":

		return "\nIlmo. Sr. %s [...]" % nome

	elif sexo.lower() == "feminino":

		return "\nIlmo. Sra. %s [...]" % nome

	else:

		return "O sexo não pôde ser identificado."

nome, sexo = input("Nome: "), input("Sexo: ")

print(tratar(nome, sexo))
