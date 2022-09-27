'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

numero_um =  float(input("Digite um numero: "))
numero_dois =  float(input("Digite um outro numero: "))



print("{}OPERADOR{}".format("#" * 10,"#" * 10))
print(" 1 - SOMA")
print(" 2 - SUBTRAÇÃO")
print(" 3 - MULTIPLICAÇÃO")
print(" 4 - DIVISÃO")
print(" 5 - POTENCIA")

opt = int(input("Digite o numero do qual operador deseja usar: "))


if opt == 1:
    resultado = numero_um + numero_dois
elif opt == 2:
    resultado = numero_um - numero_dois
elif opt == 3:
    resultado = numero_um * numero_dois
elif opt == 4:
    resultado =  numero_um / numero_dois
elif opt == 5:
   resultado =  numero_um ** numero_dois
else:
    print('INVALIDO')
print(f"O resultado e {resultado}")

if resultado % 2 == 0:
    print(f"O numero {resultado} e PAR")
else:
    print(f"O numero {resultado} e IMPAR")

if resultado < 0:
    print(f"O numero {resultado} e NEGATIVO")
else:
    print(f"O numero {resultado} e POSITIVO")

if type(resultado) == "<class 'int'>":
    print(f"O numero {resultado} e INTEIRO ")
else:
    print(f"O numero {resultado} e DECIMAL")
