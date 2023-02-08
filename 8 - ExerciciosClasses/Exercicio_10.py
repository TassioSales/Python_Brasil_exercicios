"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""


class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        self.quantidadeCombustivel -= litros
        return litros

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        return valor

    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel

    def alterarQuantidadeCombustivel(self, quantidade):
        self.quantidadeCombustivel = quantidade

    def __str__(self):
        return f"Tipo de combustivel: {self.tipoCombustivel}\nValor do litro: {self.valorLitro}\nQuantidade de combustivel: {self.quantidadeCombustivel}"


if __name__ == '__main__':
    bomba = BombaCombustivel("Gasolina", 4.50, 1000)
    print(bomba)
    print(f"Abastecendo por valor: {bomba.abastecerPorValor(100)}")
    print(f"Abastecendo por litros: {bomba.abastecerPorLitro(100)}")
    bomba.alterarValor(5.50)
    bomba.alterarCombustivel("Alcool")
    bomba.alterarQuantidadeCombustivel(500)
    print(bomba)
