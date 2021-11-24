#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Digite um numero de 1 a 7 "))
print("Esse dia da semana correponde ah")

if numero == 1:
    print("1 - Domingo")
elif numero == 2:
    print("2 - Segunda")
elif numero == 3:
    print("3 - Terça")
elif numero == 4:
    print("4 - Quarta")
elif numero == 5:
    print("5 - Quinta")
elif numero == 6:
    print("6 - Sexta")
elif numero == 7:
    print("7 - Sabado")
else:
    print("Numero invalido")