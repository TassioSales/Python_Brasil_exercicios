"""Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes
atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque;
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."""


class ContaCorrente:
    import datetime
    import random

    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        self.historico = []
        self.historico.append(f'Conta criada em {self.datetime.datetime.now()}')

    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self, numero_conta):
        self._numero_conta = numero_conta

    @property
    def nome_correntista(self):
        return self._nome_correntista

    @nome_correntista.setter
    def nome_correntista(self, nome_correntista):
        self._nome_correntista = nome_correntista

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    #criar um método para gerar um número aleatório de 6 dígitos para o número da conta
    def gerar_numero_conta(self):
        self.numero_conta = self.random.randint(100000, 999999)
        self.historico.append(f'Número da conta alterado para {self.numero_conta} em {self.datetime.datetime.now()}')

    def alterar_nome(self, nome_correntista):
        self.nome_correntista = nome_correntista
        self.historico.append(f'Nome alterado para {self.nome_correntista} em {self.datetime.datetime.now()}')

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(f'Depósito de {valor} em {self.datetime.datetime.now()}')

    def saque(self, valor):
        if self.saldo >= valor:
                    self.saldo -= valor
                    self.historico.append(f'Saque de {valor} em {self.datetime.datetime.now()}')
        else:
            print('Saldo insuficiente')

    def extrato(self):
        print(f'Extrato da conta {self.numero_conta} de {self.nome_correntista}')
        for i in self.historico:
            print(i)
        print(f'Saldo: {self.saldo}')

    def transferencia(self, conta_destino, valor):
        if self.saldo >= valor:
            self.saque(valor)
            conta_destino.deposito(valor)
            self.historico.append(f'Transferência de {valor} para a conta {conta_destino.numero_conta} em {self.datetime.datetime.now()}')
        else:
            print('Saldo insuficiente')

    def __str__(self):
        return f'Conta: {self.numero_conta} - Correntista: {self.nome_correntista} - Saldo: {self.saldo}'

    def __repr__(self):
        return f'Conta: {self.numero_conta} - Correntista: {self.nome_correntista} - Saldo: {self.saldo}'

    def __eq__(self, other):
        return self.numero_conta == other.numero_conta


if __name__ == '__main__':
    conta1 = ContaCorrente(123456, 'João')
    conta2 = ContaCorrente(654321, 'Maria')
    conta1.gerar_numero_conta()
    conta1.alterar_nome('João da Silva')
    conta1.deposito(1000)
    conta1.saque(500)
    conta1.extrato()
    conta1.transferencia(conta2, 200)
    conta1.extrato()
    conta2.extrato()
    print(conta1)
    print(conta2)


