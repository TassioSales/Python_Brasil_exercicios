"""Faça um programa que leia e valide as seguintes informações:
A - Nome: maior que 3 caracteres;
B - Idade: entre 0 e 150;
C - Salário: maior que zero;
D - Sexo: 'f' ou 'm';
E - Estado Civil: 's', 'c', 'v', 'd';"""


def nome_valido():
    while True:
        nome = input('Digite seu nome: ')
        if len(nome) > 3:
            break
        print('Nome inválido!')
    return nome


def idade_valida():
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            if 0 <= idade <= 150:
                break
        except ValueError:
            print('Idade inválida!')
        else:
            print('Idade inválida!')
    return idade


def salario_valido():
    while True:
        try:
            salario = float(input('Digite seu salário: '))
            if salario > 0:
                break
        except ValueError:
            print('Salário inválido!')
        else:
            print('Salário inválido!')
    return salario


def sexo_valido():
    while True:
        sexo = input('Digite seu sexo: ').split()[0].lower()
        if sexo == 'f' or sexo == 'm':
            break
        print('Sexo inválido!')
    return sexo


def estado_civil_valido():
    while True:
        estado_civil = input('Digite seu estado civil: ').split()[0].lower()
        if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
            break
        print('Estado civil inválido!')
    return estado_civil

if __name__ == '__main__':
    nome = nome_valido()
    idade = idade_valida()
    salario = salario_valido()
    sexo = sexo_valido()
    estado_civil = estado_civil_valido()
    print(f'Nome: {nome},; Idade: {idade}, Salário: {salario}, Sexo: {sexo}, Estado Civil: {estado_civil}')
