#parte1 O que será impresso pelos algoritmos a seguir:
def Mensagem():
  x = 10
  y = 1
  x -= 1
  y += 2
  x = x - 1
  y = y + 2
  x = x - 1
  y = y + 2
  return "x=" + str(x) + " e y=" + str(y)
print(Mensagem())
