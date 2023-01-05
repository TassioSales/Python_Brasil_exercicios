"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores"""

def impares(vetor):
    vetorImpar = []
    for item in vetor:
        if item % 2 != 0:
            vetorImpar.append(item)
    print(f"Vetor Impar: {vetorImpar}")
    
def pares(vetor):
    vetorPar = []
    for item in vetor:
        if item % 2 == 0:
            vetorPar.append(item)
    print(f"Vetor Par: {vetorPar}")
    
def lervetor(vetor):
    print(f"Valores {vetor}")

import random

#criar uma lista com 20 numeros aleatorios
listaNumeros = []
for i in range(50):
    listaNumeros.append(random.randint(0,200))
    
lervetor(listaNumeros)
pares(listaNumeros)
impares(listaNumeros)

