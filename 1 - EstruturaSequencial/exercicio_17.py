# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere  que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
#  valores para cima, isto é, considere latas cheias.


valor_lata = 80.00
valor_galoes = 25.00
capacidade_da_lata = 18
litro_para_cada_metros = 6
capacidade_dos_galoes = 3.6

metros =  float(input("Digite quantos metros quadrados deseja pintar: "))

litros =  metros / litro_para_cada_metros

latas = litros / capacidade_da_lata
galoes = litros / capacidade_dos_galoes

if latas % 18 != 0:
    latas += 1
preco = latas * valor_lata

if galoes % 3.6 != 0:
    galoes += 1
preco2 = galoes * valor_galoes


mistura_lata = int(litros / capacidade_da_lata)
mistura_galao = int((litros - (mistura_lata * capacidade_da_lata)) / capacidade_dos_galoes)

if litros - (mistura_lata * capacidade_da_lata) % capacidade_dos_galoes != 0:
    mistura_galao += 1

latas = int(latas)
galoes = int(galoes)

print(f'Apenas latas de 18 litros: {latas:.2f}, preço: R$ {preco:.2f}')
print(f'Apenas galões de 3.6 litros: {galoes:.2f}, preço: R$ {preco2:.2f}')

valor_mistura = (mistura_lata * valor_lata) + (mistura_galao * valor_galoes)

print(f'Mistura Latas: {mistura_lata:.2f} e Galoes: {mistura_galao:.2f} = R$ {valor_mistura:.2f}')