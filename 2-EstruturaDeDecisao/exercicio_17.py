# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
# bissexto.

from datetime import date
ano = int(input("Digite que ano deseja analisar: ou digite 0 para o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} e BISSEXTO')

else:
    print(f'O ano {ano} NÃO e BISSEXTO')