# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a 
# mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("digite aqui o Turno que voce estuda M-matutino ou V-Vespertino ou N- Noturno: ").upper().strip()[0]

if turno == "M":
    print("VOCE ESTUDA NO PERIODO MATUTINO")
elif turno == "V":
    print("VOCE ESTUDA NO PERIODO VESPERTINO")
elif turno == "N":
    print("VOCE ESTUDA NO PERIODO NOTURNO")
else: 
    print("PERIODO INVALIDO")