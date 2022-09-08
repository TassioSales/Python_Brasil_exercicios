"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que
o usuário digite o salário inicial do funcionário."""


def salario_atual():
    """Função que calcula o salário atual de um funcionário"""
    salario = int(input('Digite o salário inicial do funcionário: '))
    ano = 1995
    while ano <= 2022:
        print(f'Ano: {ano} - Salário: R$ {salario:.2f}')
        salario += salario * 0.015
        ano += 1


if __name__ == '__main__':
    salario_atual()
