#19. Escreva	uma	função	que	recebe	a	cor	de	um	sinal	de	trânsito	(“V”	é	verde;	“A”	é	amarelo;	“E”	é	vermelho)	e	
#retorne	a	respectiva	mensagem	“Siga”,	“Atenção”,	ou	“Pare”.	Assuma	entradas	válidas.
def sema(cor):

	if cor == "V":

		return "Siga"

	elif cor == "A":

		return "Atenção"

	elif cor == "E":

		return "Pare"

cor = input("Escreva a letra correspondente à atual cor do semáforo (use 'V' para verde, 'A' para amarelo e 'E' para vermelho): ")

if sema(cor) == None:

	print("O caractere fornecido não corresponde a nenhuma cor.")

else:

	print(sema(cor))
