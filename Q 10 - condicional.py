#10. Escreva	 uma	 função	 que	 recebe	 a	 distância	 (em	 Km)	 e	 o	 tempo	 (em	 horas)	 de	 uma	 viagem,	 e	 retorne	 a	
#velocidade	média	da	viagem
def veloc(d, t):

	return d / t

d, t = float(input("Escreva os valores correspondentes à distância (em km) e ao tempo (em h), respectivamente, da viagem: ")), float(input())

veloc = str(veloc(d, t))
veloc = veloc.rstrip('0').rstrip('.')

print("A velocidade escalar média nessa viagem foi de %s km/h." % veloc)
