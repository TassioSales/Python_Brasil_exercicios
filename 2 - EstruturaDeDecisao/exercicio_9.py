# Faça um Programa que leia três números e mostre-os em ordem decrescente

preco1 = float(input("Digite o valor do primeiro produto: "))
preco2 = float(input("Digite o valor do segundo produto: "))
preco3 = float(input("Digite o valor do terceiro produto: "))

if preco1 < preco2  and preco2 < preco3:
    print(preco1, preco2, preco3)
elif preco1 < preco3  and preco3 < preco2:
    print(preco1, preco3, preco2)
elif preco2 < preco1 and preco1 < preco3:
    print(preco2, preco1, preco3)
elif preco2 < preco3 and preco3 < preco1:
    print(preco2, preco3, preco1)
elif preco3 < preco1 and preco1 < preco2:
    print(preco3, preco1, preco2)
elif preco3 < preco2 and preco2 < preco1:
    print(preco3, preco2, preco1)c