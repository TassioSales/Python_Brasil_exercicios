#criar tabela
import mysql.connector
#nome, idade, sexo, altura, peso

def criarTabela():
    try:
        con = mysql.connector.connect(host='localhost', database='teste', user='root', password='')
        if con.is_connected():
            cursor = con.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS pessoas (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), idade INT, sexo VARCHAR(1), altura FLOAT, peso FLOAT)')
            cursor.close()
            con.close()
    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    criarTabela()





