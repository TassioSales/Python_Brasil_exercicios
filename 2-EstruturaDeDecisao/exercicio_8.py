# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Digite o valor do primeiro produto: "))
preco2 = float(input("Digite o valor do segundo produto: "))
preco3 = float(input("Digite o valor do terceiro produto: "))

menor_valor = preco1

if preco2 < menor_valor:
    menor_valor = preco2
if preco3 < menor_valor:
    menor_valor = preco3

print(f"O produto com menor valor e o com valor de {menor_valor}")