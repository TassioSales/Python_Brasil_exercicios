"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
   Foram obtidos os seguintes dados:
    A.Código da cidade;
    B.Número de veículos de passeio (em 1999);
    C.Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    D.Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    E.Qual a média de veículos nas cinco cidades juntas;
    F.Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
from numpy import mean


def acidentesTransito():
    cidades = {'Código': [], 'Veículos': [], 'Acidentes': []}
    for i in range(5):
        codigo = int(input('Código da cidade: '))
        veiculos = int(input('Número de veículos de passeio: '))
        acidentes = int(input('Número de acidentes de trânsito com vítimas: '))
        cidades['Código'].append(codigo)
        cidades['Veículos'].append(veiculos)
        cidades['Acidentes'].append(acidentes)
    print(
        f'A cidade com maior índice de acidentes é {cidades["Código"][cidades["Acidentes"].index(max(cidades["Acidentes"]))]} com {max(cidades["Acidentes"])} acidentes')
    print(
        f'A cidade com menor índice de acidentes é {cidades["Código"][cidades["Acidentes"].index(min(cidades["Acidentes"]))]} com {min(cidades["Acidentes"])} acidentes')
    print(f'A média de veículos nas cinco cidades é {mean(cidades["Veículos"])}')
    print(
        f'A média de acidentes nas cidades com menos de 2.000 veículos é {mean([cidades["Acidentes"][i] for i in range(len(cidades["Acidentes"])) if cidades["Veículos"][i] < 2000])}')


if __name__ == '__main__':
    acidentesTransito()
