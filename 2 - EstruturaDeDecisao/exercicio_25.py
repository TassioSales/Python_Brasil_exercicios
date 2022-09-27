"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

soma_negativo = 0

print("SIM OU NÂO")
pergunta_1 = str(input("Telefonou para a vítima?")).upper().split()[0]
pergunta_2 = str(input("Esteve no local do crime?")).upper().split()[0]
pergunta_3 = str(input("Mora perto da vítima?")).upper().split()[0]
pergunta_4 = str(input("Devia para a vítima?")).upper().split()[0]
pergunta_5 = str(input("Já trabalhou com a vítima?")).upper().split()[0]

if pergunta_1 == "S":
    soma_negativo += 1
if pergunta_2 == "S":
    soma_negativo += 1
if pergunta_3 == "S":
    soma_negativo += 1
if pergunta_4 == "S":
    soma_negativo += 1
if pergunta_5 == "S":
    soma_negativo += 1

if soma_negativo == 2:
    print("Suspeita")
elif somanego_negativo == 3 or somanego_negativo == 4:
    print('Cúmplice')
elif soma_negativo == 5:
    print('Assassino')
else:
    print('Inocente')

print(soma_negativo)



