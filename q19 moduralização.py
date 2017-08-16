#19. Recebe a hora atual no formado HHMM e mostre quantos minutos passaram-se desde início do dia
def min(hh, mm):

	return (hh * 60) + mm

try:

	hh, mm = float(input("Escreva o valor correspondente à hora atual: ")), float(input("Forneça o valor correspondente ao minuto atual: "))

	print("Se passaram %d minutos desde o início do dia." % min(hh, mm))

except:

	print(" não forneceu valores reais.")
