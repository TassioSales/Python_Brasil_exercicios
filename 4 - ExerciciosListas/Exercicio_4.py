"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."""

def vericaConsontes(vetor):
    consoantes = 0
    listaConsoantes = []
    for item in vetor:
        if item not in "aeiouAEIOU":
            consoantes += 1
            listaConsoantes.append(item)
    print(f"Consoantes: {consoantes}")
    print(f"Lista de consoantes: {listaConsoantes}")
    
    
#criar uma lista com 1000 caracteres aleatorios
import random
import string

listaCaracteres = []

for i in range(1000):
    listaCaracteres.append(random.choice(string.ascii_letters))
    
vericaConsontes(listaCaracteres)