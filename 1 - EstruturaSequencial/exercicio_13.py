#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo (H) homem (M) mulher: ").upper().strip()

peso_ideal_H = (72.7 * altura) - 58

peso_ideal_M = (62.1 * altura) - 44.7

if sexo == "H":
    print(f"Seu peso ideal e {peso_ideal_H:.2f}")
elif sexo == "M":
    print(f"Seu peso ideal e  {peso_ideal_M:.2f}")
else:
    print("Sexo invalido tente novamente")