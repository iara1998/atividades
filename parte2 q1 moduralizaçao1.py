#parte2 q1 O que será impresso pelos algoritmos a seguir:
def DemoFuncao(b):
  a = (b * 2)
  b = b + 5
  c = a - b
  return "a = %d;b = %d;c = %d" % (a, b, c)
print(DemoFuncao(0))
print(DemoFuncao(5))
print(DemoFuncao(10))
print(DemoFuncao(15))
print(DemoFuncao(20))
