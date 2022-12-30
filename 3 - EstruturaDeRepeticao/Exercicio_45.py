"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa."""

def menu():
    print('1 - A')
    print('2 - B')
    print('3 - C')
    print('4 - D')
    print('5 - E')
    print('0 - Sair')
    print('')
    opt = int(input('Digite a opção desejada: '))
    if opt == 0:
        exit()
    return opt

def questoes():
    listarespostas = []
    for i in range(10):
        print(f"Digite a resposta da questão {i}")
        opt = menu()
        listarespostas.append(opt)
    return listarespostas

def gabarito():
    listagabarito = []
    for i in range(10):
        print(f"Digite o resultado da Questão {i}")
        opt = menu()
        listagabarito.append(opt)
    return listagabarito

def verificarAcertos(listagabarito, listarespostas):
    acertos = 0
    for i in range(10):
        if listagabarito[i] == listarespostas[i]:
            acertos += 1
    return acertos

def verificarErros(listagabarito, listarespostas):
    erros = 0
    for i in range(10):
        if listagabarito[i] != listarespostas[i]:
            erros += 1
    return erros

def resultado():
    listagabarito = gabarito()
    listarespostas = questoes()
    acertos = verificarAcertos(listagabarito, listarespostas)
    erros = verificarErros(listagabarito, listarespostas)
    print(f'Acertos: {acertos}')
    print(f'Erros: {erros}')
    print(f'Percentual de acertos: {acertos / 10 * 100}%')
    print(f'Percentual de erros: {erros / 10 * 100}%')
    

def main():
    resultado()


if __name__ == '__main__':
    main()