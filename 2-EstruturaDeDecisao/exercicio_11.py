"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    1-salários até R$ 280,00 (incluindo) : aumento de 20%
    2-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    3-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    4-salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    5-o salário antes do reajuste;
    6-o percentual de aumento aplicado;
    7-o valor do aumento;
    8-o novo salário, após o aumento."""


salario =  float(input("Digite aqui o valor do salario atual: "))

print(f"Seu salario atual e R$ {salario}")
if salario < 280:
    salario = salario + (salario * 20 /100)
    print(f"Seu salario recebera um aumento de 20% voce passara a receber R$ {salario}")
elif salario >=280 and salario < 700:
    salario = salario + (salario * 15 /100)
    print(f"Seu salario recebera um aumento de 15% voce passara a receber R$ {salario}")
elif salario >=700 and salario < 1500:
    salario = salario + (salario * 10 /100)
    print(f"Seu salario recebera um aumento de 10% voce passara a receber R$ {salario}")
elif salario > 1500:
    salario = salario + (salario * 5 /100)
    print(f"Seu salario recebera um aumento de 5% voce passara a receber R$ {salario}")