"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

def dadosfuncionario():
    qtdfuncionarios = int(input("Quantos funcionários tem na empresa? "))
    salarios = []
    for funcionario in range(qtdfuncionarios):
        salario = float(input("Qual o salário do funcionário {fucionario}? "))
        salarios.append(salario)
    return salarios

def calculaSalario(salarios):
    salariosCalculados = []
    for salario in salarios:
        salario = (salario * 0.09) + salario
        salariosCalculados.append(salario)
    return salariosCalculados

def calculaFaixaSalario(salariosCalculados):
    salario200_299 = [sl for sl in salariosCalculados if sl >= 200 and sl <= 299]
    salario300_399 = [sl for sl in salariosCalculados if sl >= 300 and sl <= 399]
    salario400_499 = [sl for sl in salariosCalculados if sl >= 400 and sl <= 499]
    salario500_599 = [sl for sl in salariosCalculados if sl >= 500 and sl <= 599]
    salario600_699 = [sl for sl in salariosCalculados if sl >= 600 and sl <= 699]
    salario700_799 = [sl for sl in salariosCalculados if sl >= 700 and sl <= 799]
    salario800_899 = [sl for sl in salariosCalculados if sl >= 800 and sl <= 899]
    salario900_999 = [sl for sl in salariosCalculados if sl >= 900 and sl <= 999]
    salario1000 = [sl for sl in salariosCalculados if sl >= 1000]
    print(f"Salários entre 200 e 299: {len(salario200_299)}")
    print(f"Salários entre 300 e 399: {len(salario300_399)}")
    print(f"Salários entre 400 e 499: {len(salario400_499)}")
    print(f"Salários entre 500 e 599: {len(salario500_599)}")
    print(f"Salários entre 600 e 699: {len(salario600_699)}")
    print(f"Salários entre 700 e 799: {len(salario700_799)}")
    print(f"Salários entre 800 e 899: {len(salario800_899)}")
    print(f"Salários entre 900 e 999: {len(salario900_999)}")
    print(f"Salários entre 1000: {len(salario1000)}")
    
    
def main():
    salarios = dadosfuncionario()
    salariosCalculados = calculaSalario(salarios)
    calculaFaixaSalario(salariosCalculados)

    
    
        

if __name__ == '__main__':
    main()
    
    