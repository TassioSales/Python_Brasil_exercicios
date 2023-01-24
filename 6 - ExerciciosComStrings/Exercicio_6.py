"""Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com
o nome do mês por extenso."""


def lerData():
    try:
        data = input('Digite sua data de nascimento (dd/mm/aaaa): ')
        if len(data) != 10:
            raise ValueError
        dia = int(data[:2])
        mes = int(data[3:5])
        ano = int(data[6:])
        if dia < 1 or dia > 31:
            raise ValueError
        if mes < 1 or mes > 12:
            raise ValueError
        if ano < 1:
            raise ValueError
        return dia, mes, ano
    except ValueError:
        print('Data inválida.')
        return lerData()
    except IndexError:
        print('Data inválida.')
        return lerData()
    except Exception as e:
        print('Erro desconhecido: {}'.format(e))
        return lerData()


def dataExtenso(dia, mes, ano):
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
             9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    print('{} de {} de {}'.format(dia, meses[mes], ano))


def main():
    dia, mes, ano = lerData()
    dataExtenso(dia, mes, ano)


if __name__ == '__main__':
    main()
