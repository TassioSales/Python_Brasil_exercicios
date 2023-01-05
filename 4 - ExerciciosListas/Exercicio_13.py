"""Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""

#função para de janeiro a dezembro com temperaturas aleatorias entre 0 e 45 e retorna uma lista com as temperaturas de cada mes do ano
def temperaturasAno():
         #criar uma lista com os meses do ano
    meses = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    listaTemperaturas = []
    for i in range(12):
        import random
        temperatura = random.randint(0,45)
        listaTemperaturas.append([meses[i],temperatura])
    return listaTemperaturas

#função para calcular a media das temperaturas do ano
def mediaTemperaturas(listaTemperaturas):
    soma = 0
    for item in listaTemperaturas:
        soma += item[1]
    return soma/len(listaTemperaturas)  

#função para mostrar as temperaturas acima da media do ano
def temperaturasAcimaMedia(listaTemperaturas):
    media = mediaTemperaturas(listaTemperaturas)
    print(f"Temperaturas acima da media do ano: ")
    #mostrar a temperatura media do ano
    print(f'A Temperatura media do ano foi {media:.2f}°')
    for item in listaTemperaturas:
        if item[1] > media:
            print(f"{item[0]}: {item[1]}°")
    
def main():
    listaTemperaturas = temperaturasAno()
    print(f"Lista de temperaturas: {listaTemperaturas}")
    temperaturasAcimaMedia(listaTemperaturas)

if __name__ == '__main__':
    main()