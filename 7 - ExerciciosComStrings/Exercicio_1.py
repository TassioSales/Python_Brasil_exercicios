"""Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
relatório dos endereços IP válidos e inválidos. O arquivo de entrada possui o seguinte formato: 200.135.80.9


O arquivo de saída possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256"""

import re


# função para ler o arquivo e retorna uma lista com os ips
def lerArquivo():
    try:
        with open('ips.txt', 'r') as arquivo:
            ips = arquivo.readlines()
            # remove o \n do final da string
            ips = [ip.replace('\n', '') for ip in ips]
            # transforma a lista em um set para remover os ips duplicados
            ips = set(ips)
            # transforma o set em uma lista novamente
            ips = list(ips)
            return ips
    except Exception as e:
        print(e)
        return lerArquivo()


# calcula os ips validos e invalidos
def calculaIps(ips):
    ipsValidos = []
    ipsInvalidos = []
    for ip in ips:
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
            ipsValidos.append(ip)
        else:
            ipsInvalidos.append(ip)
    return ipsValidos, ipsInvalidos


# função para escrever o arquivo
def escreveArquivo(ipsValidos, ipsInvalidos):
    try:
        with open('ips_validos.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('[Endereços válidos:] \n')
            for ip in ipsValidos:
                arquivo.write(ip + '\n')
        with open('ips_invalidos.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.write('[Endereços inválidos:] \n')
            for ip in ipsInvalidos:
                arquivo.write(ip + '\n')
    except Exception as e:
        print(e)
        return escreveArquivo(ipsValidos, ipsInvalidos)


def main():
    ips = lerArquivo()
    ipsValidos, ipsInvalidos = calculaIps(ips)
    escreveArquivo(ipsValidos, ipsInvalidos)


if __name__ == '__main__':
    main()
