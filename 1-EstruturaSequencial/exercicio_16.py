# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que # custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

valor_lata = 80.00
capacidade_da_lata = 18
litro_para_cada_metros = 3

metros =  float(input("Digite quantos metros quadrados deseja pintar: "))

litros =  metros / litro_para_cada_metros

if litros <= 18:
    print("A quantidade de latas de tinta que voce ira gasta e 1")
    print("Valor de  R$ 80.00")
else:
    latas = litros / capacidade_da_lata
    latas = int(latas)
    valor = latas * valor_lata
    print(f"A quantidade de latas de tinta que voce ira gasta e {latas}")
    print(f"Valor de  R$ {valor}")


