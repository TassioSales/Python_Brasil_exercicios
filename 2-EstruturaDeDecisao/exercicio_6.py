# Faça um Programa que leia três números e mostre o maior deles.

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"O numero {numero1} e o maior")
elif  numero2 > numero1 and  numero2 > numero3:
    print(f"O numero {numero2} eo o maior")
elif  numero3 > numero1 and  numero3 > numero2:
    print(f"O numero {numero3} eo o maior")
else:
    print("Os numeros são iguais")
