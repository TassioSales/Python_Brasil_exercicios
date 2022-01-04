#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = input("Digite um numero: ")

numero = int(numero)

if numero % 2 == 0:
    print(f"O numero {numero} e par")
else:
    print(f"O numero {numero} e impar")