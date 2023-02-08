"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no
tanque. O consumo é especificado no construtor e o nível de combustível inicial é 0. Forneça um método andar( ) que
simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível. Forneça um método adicionarGasolina( ),
para abastecer o tanque. Exemplo de uso: meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. meuFusca.andar(100);            # anda 100
quilômetros. meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque."""


class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    @property
    def combustivel(self):
        return self._combustivel

    @combustivel.setter
    def combustivel(self, valor):
        if valor < 0:
            self._combustivel = 0
        else:
            self._combustivel = valor

    @property
    def consumo(self):
        return self._consumo

    @consumo.setter
    def consumo(self, valor):
        if valor < 0:
            self._consumo = 0
        else:
            self._consumo = valor

    def andar(self, distancia):
        self.combustivel -= distancia / self.consumo
        print(f"O carro andou {distancia}km e ainda tem {self.combustivel:.2f} litros de combustivel")

    def obterGasolina(self):
        print(f"O carro tem {self.combustivel:.2f} litros de combustivel")

    def adicionarGasolina(self, litros):
        self.combustivel += litros
        print(f"O carro foi abastecido com {litros} litros de combustivel")


if __name__ == "__main__":
    meuFusca = Carro(15)
    meuFusca.adicionarGasolina(20)
    meuFusca.andar(100)
    meuFusca.obterGasolina()
    meuFusca.andar(100)

