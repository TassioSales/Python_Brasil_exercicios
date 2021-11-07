
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do 
# seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, # faça um programa que nos dê:

#   salário bruto.
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
#   calcule os descontos e o salário líquido, conforme a tabela abaixo

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$


valor_por_hora_trabalhada = float(input("Digite o valor que voce ganha por hora trabalhada R$ "))
horas_trabalhdas_mes = float(input("Digite quantas horas voce trabalhou esses mes: "))

salario_bruto =  valor_por_hora_trabalhada * horas_trabalhdas_mes

ir = (salario_bruto * 11 / 100)
inss = (salario_bruto * 8 / 100)
sindicato = (salario_bruto * 5 / 100)
total_de_impostos =  ir + inss + sindicato
salario_liquido = salario_bruto - total_de_impostos


print(f"Salário Bruto : R${salario_bruto}")
print(f"IR (11%) : R${ir}")
print(f'INSS (8%) : R${inss}')
print(f'Sindicato ( 5%) : R${sindicato}')
print(f"Total de impostos R${total_de_impostos}")
print(f'Salário Liquido : R${salario_liquido}')