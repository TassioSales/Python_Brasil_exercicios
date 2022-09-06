"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:"""


def tabuada():
    """Função que retorna a tabuada de um número"""
    numero = int(input('Digite um número que deseja ver a tabuada: '))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if __name__ == '__main__':
    tabuada()
