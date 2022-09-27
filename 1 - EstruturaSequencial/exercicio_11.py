#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#  A)  o produto do dobro do primeiro com metade do segundo .
#  B)  a soma do triplo do primeiro com o terceiro.
#  C)  o terceiro elevado ao cubo.


numero_1 = int(input("Difite um numero inteiro: "))
numero_2 = int(input("Digite outro numero inteiro: "))
numero_3 = float(input("Digite um numero Real "))

resultado_A =   (numero_1 * 2) * (numero_2 / 2)
resultado_B =   (numero_1 * 3) + numero_3
resultado_C =   numero_3 ** 3

print(f"Produto: {resultado_A:.2f}")
print(f"Soma: {resultado_B:.2f}")
print(f"Cubo: {resultado_C:.2f}")