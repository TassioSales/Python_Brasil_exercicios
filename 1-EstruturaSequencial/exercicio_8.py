#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


ganho_por_hora = float(input("Quanto voce ganha por horas Trabalhada: "))

horas_trabalhadas = float(input("Quantas horas voce trabalho esse mes: "))

salario = ganho_por_hora * horas_trabalhadas

print(f"Seu salario esse mes deve ser aproximadamente de R$ {salario}")