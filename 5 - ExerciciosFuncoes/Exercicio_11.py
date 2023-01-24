"""Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida."""


def pededata():
    try:
        data = input("Digite uma data no formato DD/MM/AAAA: ")
        dia, mes, ano = data.split("/")
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        return dia, mes, ano
    except ValueError:
        print("Digite uma data válida no formato DD/MM/AAAA.")
        return pededata()
    except Exception as e:
        print(e)
        return pededata()


def mesPorExtenso(mes):
    meses = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho", 7: "julho", 8: "agosto",
             9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}
    return meses[mes]


def main():
    dia, mes, ano = pededata()
    print(f"{dia} de {mesPorExtenso(mes)} de {ano}")


if __name__ == "__main__":
    main()
