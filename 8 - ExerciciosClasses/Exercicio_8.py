"""Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os
métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?"""

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        for comida in self.bucho:
            print(f'{comida} ', end='')
        print()

    def digerir(self):
        self.bucho = []
        print('Bucho vazio')

    def __str__(self):
        return f'Macaco: {self.nome}'

    def __repr__(self):
        return f'Macaco: {self.nome}'

if __name__ == '__main__':
    macaco1 = Macaco('Macaco1')
    macaco2 = Macaco('Macaco2')
    macaco1.comer('banana')
    macaco1.comer('maçã')
    macaco1.comer('pera')
    macaco1.verBucho()
    macaco1.digerir()
    macaco1.verBucho()
    macaco2.comer('banana')
    macaco2.comer('maçã')
    macaco2.comer('pera')
    macaco2.verBucho()
    macaco2.digerir()
    macaco2.verBucho()
    macaco1.comer(macaco2)
    macaco1.verBucho()