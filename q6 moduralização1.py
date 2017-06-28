#q6 Recebe uma velocidade em km/h, retorne esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)
def velocidade(x):
    return (x / 3.6)
b = float(input("Digite a velocidade em km/h"))
b = velocidade(b)
        
print("valor em m/s e:",b)
