# -*- coding: utf-8 -*-
print ("Efetue o cálculo e a apresentação do valor de uma prestação em atraso utilizando a fórmula PRETAÇÃO = VALOR + (VALOR * (TAXA / 100) * TEMPO)")
v= int(input("Digite o valor da Prestação"))
t= int(input("Digite o numero de dias em atraso"))
ta= int(input("Digite a taxa:"))
p = v + (v * (ta / 100) * t)
print "O valor da prestação com atraso foi de %s" %p