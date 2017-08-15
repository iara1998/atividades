#17. A	partir	de	dois	números	fornecidos	pelo	usuário,	escreva	uma	das	seguintes	mensagens:
#Os	dois	são	pares
#Os	dois	são	impares
#O primeiro	é	par	e	o	segundo	é	ímpar
#O  primeiro	é	ímpar	e	o	segundo	é	par
def nums(a, b):

	if a % 2 == 0 and b % 2 == 0:

		return "Os dois são pares"

	elif a % 2 != 0 and b % 2 != 0:

		return "Os dois são ímpares"

	elif a % 2 == 0 and b % 2 != 0:

		return "O primeiro é par e o segundo é ímpar"

	elif a % 2 != 0 and b % 2 == 0:

		return "O primeiro é ímpar e o segundo é par"

try:

	a, b = int(input("Forneça dois números inteiros: ")), int(input())

	print(nums(a, b))

except:

	print("Não foram fornecidos valores inteiros.")
