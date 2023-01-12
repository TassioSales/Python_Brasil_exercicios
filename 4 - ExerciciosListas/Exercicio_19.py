"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""


def menu():
    try:
        listaopt = []
        print('''
        1- Windows Server
        2- Unix
        3- Linux
        4- Netware
        5- Mac OS
        6- Outro
        0- Sair
        ''')
        while True:
            opt = int(input('Digite a opção desejada: '))
            if opt == 0:
                break
            elif opt > 6:
                print('Opção inválida!')
            else:
                listaopt.append(opt)
    except ValueError:
        print('Opção inválida!')
        pass
    except Exception as erro:
        print(f'Erro encontrado: {erro.__class__}')
        pass
    
    return listaopt

def contaVotos(listaVotos):
    Windows = 0
    Unix = 0
    Linux = 0
    Netware = 0
    Mac = 0
    Outro = 0
    for voto in listaVotos:
        if voto == 1:
            Windows += 1
        elif voto == 2:
            Unix += 1
        elif voto == 3:
            Linux += 1
        elif voto == 4:
            Netware += 1
        elif voto == 5:
            Mac += 1
        elif voto == 6:
            Outro += 1
    return Windows, Unix, Linux, Netware, Mac, Outro

def calculaPercentual(listaVotos):
    total = len(listaVotos)
    Windows, Unix, Linux, Netware, Mac, Outro = contaVotos(listaVotos)
    percentWindows = (Windows / total) * 100
    percentUnix = (Unix / total) * 100
    percentLinux = (Linux / total) * 100
    percentNetware = (Netware / total) * 100
    percentMac = (Mac / total) * 100
    percentOutro = (Outro / total) * 100
    return percentWindows, percentUnix, percentLinux, percentNetware, percentMac, percentOutro

def vencedor(listaVotos):
    Windows, Unix, Linux, Netware, Mac, Outro = contaVotos(listaVotos)
    if Windows > Unix and Windows > Linux and Windows > Netware and Windows > Mac and Windows > Outro:
        return 'Windows Server'
    elif Unix > Windows and Unix > Linux and Unix > Netware and Unix > Mac and Unix > Outro:
        return 'Unix'
    elif Linux > Windows and Linux > Unix and Linux > Netware and Linux > Mac and Linux > Outro:
        return 'Linux'
    elif Netware > Windows and Netware > Unix and Netware > Linux and Netware > Mac and Netware > Outro:
        return 'Netware'
    elif Mac > Windows and Mac > Unix and Mac > Linux and Mac > Netware and Mac > Outro:
        return 'Mac OS'
    elif Outro > Windows and Outro > Unix and Outro > Linux and Outro > Netware and Outro > Mac:
        return 'Outro'
    
def imprimirResultado(listaVotos):
    Windows, Unix, Linux, Netware, Mac, Outro = contaVotos(listaVotos)
    percentWindows, percentUnix, percentLinux, percentNetware, percentMac, percentOutro = calculaPercentual(listaVotos)
    print('''
    Sistema Operacional     Votos   %
    -------------------     -----   ---
    Windows Server           {}   {:.2f}%
    Unix                     {}   {:.2f}%
    Linux                    {}   {:.2f}%
    Netware                  {}    {:.2f}%
    Mac OS                   {}    {:.2f}%
    Outro                    {}    {:.2f}%
    -------------------     -----
    Total                    {}
    '''.format(Windows, percentWindows, Unix, percentUnix, Linux, percentLinux, Netware, percentNetware, Mac, percentMac, Outro, percentOutro, len(listaVotos)))
    print(f'O Sistema Operacional mais votado foi o {vencedor(listaVotos)}, com {max(Windows, Unix, Linux, Netware, Mac, Outro)} votos, correspondendo a {max(percentWindows, percentUnix, percentLinux, percentNetware, percentMac, percentOutro):.2f}% dos votos.')

    
def main():
    listaVotos = menu()
    imprimirResultado(listaVotos)
    
if __name__ == '__main__':
    main()
