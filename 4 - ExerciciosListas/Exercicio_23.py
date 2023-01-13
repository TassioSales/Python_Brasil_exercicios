"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
"""

def lerArquivo():
    try:
        arquivo = open('usuarios.txt', 'r')
        linhas = arquivo.readlines()
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        pass
    except Exception as erro:
        print(f'Erro encontrado: {erro.__class__}')
        pass
    return linhas


#função para calcular o espaço ocupado por cada usuário
def calculaEspaco(linhas):
    listaEspaco = []
    for linha in linhas:
        listaEspaco.append(float(linha.split()[1]))
    return listaEspaco

#função para calcular o espaço médio ocupado
def calculaMedia(listaEspaco):
    return sum(listaEspaco) / len(listaEspaco)


#função para calcular o espaço total ocupado
def calculaTotal(listaEspaco):
    return sum(listaEspaco)


#função para calcular a porcentagem de espaço ocupado por cada usuário
def calculaPorcentagem(listaEspaco):
    listaPorcentagem = []
    for espaco in listaEspaco:
        listaPorcentagem.append(espaco / calculaTotal(listaEspaco) * 100)
    return listaPorcentagem

#função para escrever o relatório
def escreveRelatorio(linhas, listaEspaco, listaPorcentagem):
    try:
        arquivo = open('relatorio.txt', 'w')
        arquivo.write('ACME Inc.               Uso do espaço em disco pelos usuários \n')
        arquivo.write('-' * 80 + ' \n')
        arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso \n')
        for i in range(len(linhas)):
            arquivo.write(f'{i + 1:<4} {linhas[i].split()[0]:<15} {listaEspaco[i]:>10.2f} MB {listaPorcentagem[i]:>18.2f}% \n')
        arquivo.write(f'\nEspaço total ocupado: {calculaTotal(listaEspaco):.2f} MB \n')
        arquivo.write(f'Espaço médio ocupado: {calculaMedia(listaEspaco):.2f} MB \n')
    except Exception as erro:
        print(f'Erro encontrado: {erro.__class__}')
        pass
        

def main():
    linhas = lerArquivo()
    listaEspaco = calculaEspaco(linhas)
    listaPorcentagem = calculaPorcentagem(listaEspaco)
    escreveRelatorio(linhas, listaEspaco, listaPorcentagem)
    

if __name__ == '__main__':
    main()
                 
            
                          
    
    
                            
        
    

    
