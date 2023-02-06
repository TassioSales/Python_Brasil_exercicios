import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class Criapdf:
    def __init__(self, nome, cpf, endereco, bairro, cidade, estado, cep, telefone, email, data, hora, servico, valor,
                 obs, total):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.telefone = telefone
        self.email = email
        self.data = data
        self.hora = hora
        self.servico = servico
        self.valor = valor
        self.obs = obs
        self.total = total

    def salva_arquivo(self):
        arquivo = open('orcamento.txt', 'w', encoding='utf-8')
        arquivo.write('Nome: ' + self.nome + '\n')
        arquivo.write('CPF: ' + self.cpf + '\n')
        arquivo.write('Endereço: ' + self.endereco + '\n')
        arquivo.write('Bairro: ' + self.bairro + '\n')
        arquivo.write('Cidade: ' + self.cidade + '\n')
        arquivo.write('Estado: ' + self.estado + '\n')
        arquivo.write('CEP: ' + self.cep + '\n')
        arquivo.write('Telefone: ' + self.telefone + '\n')
        arquivo.write('E-mail: ' + self.email + '\n')
        arquivo.write('Data: ' + self.data + '\n')
        arquivo.write('Hora: ' + self.hora + '\n')
        arquivo.write('Serviço: ' + self.servico + '\n')
        arquivo.write('Valor: ' + self.valor + '\n')
        arquivo.write('Observações: ' + self.obs + '\n')
        arquivo.write('Total: ' + self.total + '\n')
        arquivo.close()
        os.startfile("orcamento.txt")

    def gerar_pdf(self):
        pdf = canvas.Canvas("orcamento.pdf", pagesize=A4)
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
        pdf.setFont('Arial', 12)
        pdf.drawString(2.5 * cm, 27 * cm, 'Nome: ' + self.nome)
        pdf.drawString(2.5 * cm, 26.5 * cm, 'CPF: ' + self.cpf)
        pdf.drawString(2.5 * cm, 26 * cm, 'Endereço: ' + self.endereco)
        pdf.drawString(2.5 * cm, 25.5 * cm, 'Bairro: ' + self.bairro)
        pdf.drawString(2.5 * cm, 25 * cm, 'Cidade: ' + self.cidade)
        pdf.drawString(2.5 * cm, 24.5 * cm, 'Estado: ' + self.estado)
        pdf.drawString(2.5 * cm, 24 * cm, 'CEP: ' + self.cep)
        pdf.drawString(2.5 * cm, 23.5 * cm, 'Telefone: ' + self.telefone)
        pdf.drawString(2.5 * cm, 23 * cm, 'E-mail: ' + self.email)
        pdf.drawString(2.5 * cm, 22.5 * cm, 'Data: ' + self.data)
        pdf.drawString(2.5 * cm, 22 * cm, 'Hora: ' + self.hora)
        pdf.drawString(2.5 * cm, 21.5 * cm, 'Serviço: ' + self.servico)
        pdf.drawString(2.5 * cm, 21 * cm, 'Valor: ' + self.valor)
        pdf.drawString(2.5 * cm, 20.5 * cm, 'Observações: ' + self.obs)
        pdf.drawString(2.5 * cm, 20 * cm, 'Total: ' + self.total)
        pdf.save()
        os.startfile("orcamento.pdf")


if __name__ == '__main__':
    nome = 'João'
    cpf = '123.456.789-00'
    endereco = 'Rua do João'
    bairro = 'Centro'
    cidade = 'São Paulo'
    estado = 'SP'
    cep = '12345-678'
    telefone = '(11) 1234-5678'
    email = 'joao@gmail.com'
    data = '01/01/2019'
    hora = '12:00'
    servico = 'Corte de cabelo'
    valor = 'R$ 50,00'
    obs = 'Cabelo comprido'
    total = 'R$ 50,00'
    orcamento = Criapdf(nome, cpf, endereco, bairro, cidade, estado, cep, telefone, email, data, hora, servico, valor,
                        obs, total)
    orcamento.salva_arquivo()
    orcamento.gerar_pdf()
