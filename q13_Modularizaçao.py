#13. Recebe o ano de nascimento de uma pessoa e escreva na tela a sua idade em 31/12/2013.
x=int(input("Digite o ano de nascimento"))
def nascimento(x):
    a= 2013-x
    return "Sua idade em 31/12/2013", a
print(nascimento(x))
