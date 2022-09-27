# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez 
# que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar 
# uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e 
# calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que 
# João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""

peso_do_peixe = float(input("Digite o peso do seu peixe: "))

peso_limite = 50
valor_da_multa_por_quilo = 4

if peso_do_peixe <= peso_limite:
    print(f"Seu peixe esta com {peso_do_peixe}Kg")
    print(f"Seu peixe Esta dentro dos limites permitidos pesolo estado de São Paulo")
    print(f"Que e de {peso_limite}Kg")
else:
    quilos_a_mais = peso_do_peixe - peso_limite
    multa = quilos_a_mais * valor_da_multa_por_quilo
    print(f"Seu peixe ultrapassou o peso de {peso_limite}Kg")
    print(f"Seu peixe esta com {peso_do_peixe} com {quilos_a_mais}Kg acima do permitido")
    print(f"A cada quilo acima do permitido voce tera que pagar um valor de R$ {valor_da_multa_por_quilo}")
    print(f"Voce tera que pagar uma multa de R$ {multa}")
