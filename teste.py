"""Detectar números de CPF com separador de milhares e hífen."""
import re

teste = ['000.000.000-00', '111.111.111-11', '0111.111.111-11', '11101110111-11', '111.111.111111', '1110110111111',
         '..1.11011011-11']

for cpf in teste:
    if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
        print(f'{cpf}')
    else:
        pass
