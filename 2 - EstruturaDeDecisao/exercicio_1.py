#Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"O numero {numero1} e maior que o numero {numero2}")
elif numero2  >  numero1:
    print(f"O numero {numero2} e maior que o numero {numero1}")
else:
    print(f'Os numeros são iguais')