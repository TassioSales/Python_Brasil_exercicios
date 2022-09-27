"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220."""


valor_hora = float(input("Digite aqui o valor da sua hora de trabalho: "))
horas_trabalhadas =  float(input("Digite aqui a quantidade de horas trabalhadas:  "))

salario =  valor_hora  *  horas_trabalhadas
ponto = "." * 20
#Calculando descontos


print(f"Salario Bruto: ({valor_hora} * {horas_trabalhadas}):{ponto} R$ {salario}")

if salario <= 900:
    print("Voce e isento de imposto IR")
elif salario > 900 and salario <= 1500:
    ir = (salario * 5 / 100)
    print(f"( - ) IR (5%):{ponto} R$ {ir}")
elif salario > 1500 and salario <= 2500:
    ir = (salario * 10 / 100)
    print(f"( - ) IR (10%):{ponto} R$ {ir}")
elif salario > 1500:
    ir = (salario * 20 / 100)
    print(f"( - ) IR (20%):{ponto} R$ {ir}")

inss =  (salario * 10 / 100)
print(f"( - ) INSS (10%):{ponto} R$ {inss}")
sindicato =  (salario * 3 / 100)
print(f"( - ) SINDICATO (3%):{ponto} R$ {sindicato}")
fgts =   (salario * 11 / 100)
print(f"FGTS (11%):{ponto} R$ {inss}")

total_descontos =  ir + inss + sindicato

print(f"Total de descontos:{ponto} R$ {total_descontos}")

salario_final =  salario - total_descontos

print(f" Salário Liquido:{ponto} R$ {salario_final}")
