'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3'%' por litro
acima de 20 litros, desconto de 5"%" por litro
Gasolina:
até 20 litros, desconto de 4'%' por litro
acima de 20 litros, desconto de 6'%' por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''



print("Tipo de combustivel:")
print()
print('1 - Gasolina')
print('2 - Álcool')
print()

opt = int(input("Digite o tipo de combustiveu: "))
valor_gasolina = 6.75
valor_alcool = 5.18


if opt == 1:
    print("Voce Escolheu gasolina:")
    quantidade = int(input("Quantos litros de gasolina deseja abastecer: "))
    if quantidade <= 20:
        valor =  quantidade * valor_gasolina
        valor_final = valor -  (valor * 4 / 100)
        print(f"O valor total ah pagar e {valor_final:.2f}")
    else:
        valor =  quantidade * valor_gasolina
        valor_final = valor -  (valor * 6 / 100)
        print(f"O valor total ah pagar e {valor_final:.2f}")
if opt == 2:
    print("Voce Escolheu Álcool:")
    quantidade = int(input("Quantos litros de Álcool deseja abastecer: "))
    if quantidade <= 20:
        valor =  quantidade * valor_alcool
        valor_final = valor -  (valor * 3 / 100)
        print(f"O valor total ah pagar e {valor_final:.2f}")
    else:
        valor =  quantidade * valor_alcool
        valor_final = valor -  (valor * 5 / 100)
        print(f"O valor total ah pagar e {valor_final:.2f}")
