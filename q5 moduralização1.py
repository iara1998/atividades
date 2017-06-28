#Recebe uma velocidade em m/s, retorne esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)0

def velocidade(x):
    return (x * 3.6)
b = float(input("Digite a velocidade em m/s"))
b = velocidade(b)
        
print("valor em km/h e:",b)
