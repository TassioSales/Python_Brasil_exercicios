"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""

def lervetor(vetor):
    media = sum(vetor) / len(vetor)
    print(f"Média:, {media:.2f}")
    
notas = [5,8,9,7]
notas2 = [5,8,9,7,10]
notas3 = [5,8,9,7,10,11]


lervetor(notas)
lervetor(notas2)
lervetor(notas3)