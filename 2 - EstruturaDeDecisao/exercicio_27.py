'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10'%' sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

valor_morango_ate_5kilos = 2.5
valor_morango_maior_5kilos = 2.2
valor_maca_ate_5kilos = 1.8
valor_maca_maior_5kilos = 1.5



print("#### Frutas ####")
print()
print("1 - Morango")
print("2 - Maçã")
print()

fruta = int(input("Qual fruta deseja comprar: "))
kilos = float(input("Quantos kilos voce deseja comprar: "))


