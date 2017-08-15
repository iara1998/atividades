#06. Faça um programa que leia um nome de usuário e a
#sua senha e não aceite a senha igual ao nome do
#usuário, mostrando uma mensagem de erro e
#voltando a pedir as informações.
username = input("Esvreva um nome de usuário e a sua respectiva senha (não podem ser iguais):\nUsername: ")
Senha = input("Senha: ")

while username == Senha:

	username = input("Erro: os valores não podem ser iguais.\nUsername: ")
	password = input("Senha: ")
