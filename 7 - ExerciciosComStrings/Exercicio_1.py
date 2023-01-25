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

# função para ler o arquivo
def lerArquivo():
    try:
        with open('ips.txt', 'r') as arquivo:
            return arquivo.read()
    except Exception as e:
        print(e)
        return lerArquivo()


# função para validar o ip
def validarIp(ip):
    ip_valido = []
    ip_invalido = []
    for i in ip:
        if i.count('.') == 3:
            octeto = i.split('.')
            if len(octeto) == 4:
                if 0 <= int(octeto[0]) <= 255 and 0 <= int(octeto[1]) <= 255 and 0 <= int(octeto[2]) <= 255 and 0 <= int(octeto[3]) <= 255:
                    ip_valido.append(i)
                else:
                    ip_invalido.append(i)
            else:
                ip_invalido.append(i)
        else:
            ip_invalido.append(i)




# Criar arquivo utf-8 com os ips válidos e inválidos separados por categoria



def main():
    ip = lerArquivo().split(' ')
    ip_valido, ip_invalido = validarIp(ip)
    escreverArquivo(ip_valido, ip_invalido)


if __name__ == '__main__':
    main()
