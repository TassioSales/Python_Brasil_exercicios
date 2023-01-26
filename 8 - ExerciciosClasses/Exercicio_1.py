"""Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def circunferencia(self):
        return self._circunferencia

    @circunferencia.setter
    def circunferencia(self, circunferencia):
        self._circunferencia = circunferencia

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor


if __name__ == '__main__':
    bola = Bola('azul', 10, 'plastico')
    print(f'A atual cor da bola é {bola.mostraCor()} e a circunferência é {bola.circunferencia} '
          f'e o material é {bola.material}')
    bola.trocaCor('vermelho')
    print(f'A nova cor da bola é {bola.mostraCor()} e a circunferência é {bola.circunferencia} '
          f'e o material é {bola.material}')


