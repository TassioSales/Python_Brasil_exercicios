"""Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""

class Carro:
    def __init__(self):
        self.modelo = ''
        self.km_litro = 0

    def cadastra(self):
        self.modelo = input('Nome: ')
        self.km_litro = float(input('Km por litro: '))

    def relatorio(self, posicao, litros, valor):
        print(f'{posicao} - {self.modelo} - {self.km_litro} - {litros:.1f} litros - R$ {valor:.2f}')
        
class Meta:
    def __init__(self):
        self.lista_carros = []
        self.lista_consumo = []
        self.lista_valor = []
        self.lista_litros = []
        self.menor = 0
        self.menor_consumo = 0
        self.menor_valor = 0
        self.menor_litros = 0

    def calcula(self):
        for i in range(5):
            carro = Carro()
            carro.cadastra()
            self.lista_carros.append(carro)
        for i in self.lista_carros:
            self.lista_consumo.append(i.km_litro)
        self.menor = min(self.lista_consumo)
        for i in self.lista_carros:
            if i.km_litro == self.menor:
                self.menor_consumo = i.modelo
        for i in self.lista_carros:
            self.lista_litros.append(1000/i.km_litro)
        for i in self.lista_carros:
            self.lista_valor.append((1000/i.km_litro)*2.25)
        print('Relatório Final')
        for i in range(5):
            self.lista_carros[i].relatorio(i+1, self.lista_litros[i], self.lista_valor[i])
        print(f'O menor consumo é do {self.menor_consumo}.')
        
if __name__ == '__main__':
    meta = Meta()
    meta.calcula()