#15. Crie	uma	função	que	recebe	uma	letra	e	retorna	“verdadeiro”	se	for	uma	vogal.
def vogal(l):

	return l == "a" or l == "e" or l == "i" or l == "o" or l == "u"

l = input("Escreva uma letra: ")

if len(l) == 1:

	print(vogal(l))

else:

	print("Somente uma letra deve ser fornecida.")
