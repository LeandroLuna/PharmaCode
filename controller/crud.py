import sqlite3  
from model.farmaco import Farmaco

class DbManager:
    def __init__(self):
        self.conexao = sqlite3.connect("database.dp")

    # Cria uma tabela
    def criarTabela(self):
        try:
            self.conexao.execute('''CREATE TABLE medicamentos(
            id INTEGER PRIMARY KEY, 
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL);
            ''')
        except:
            print('Já existe uma tabela criada.')
 
    # Insere um dado
    def inserirDado(self, id, nome, preco, quantidade ):
        query = ("INSERT INTO medicamentos VALUES(%s, '%s', %s, %s);"%(id, nome, preco, quantidade))
        self.conexao.execute(query)
        self.conexao.commit()

    # Injeta dados mockados no banco de dados.
    def gerarMock(self, dados):
        try:
            for dado in dados:
                self.conexao.execute(dado)
                self.conexao.commit()
        except:
            print('Houve um problema ao inserir os novos dados de teste..')

    # Recupera os dados do banco de dados
    def buscarDados(self, valor, tipo_pesquisa):
        if(tipo_pesquisa == "nome"):
            query = "SELECT * FROM medicamentos WHERE {} = '{}'".format(tipo_pesquisa, valor)
            cursor = self.conexao.execute(query)
            return cursor
        else:
            query = "SELECT * FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valor)
            cursor = self.conexao.execute(query)
            return cursor
            

    def atualizarDados(self, novoValor, valorIdentificacao, tipo_pesquisa, tipo_alteracao):
        if(tipo_pesquisa == "nome" and tipo_alteracao == "nome"):
            query = "UPDATE medicamentos SET {} = '{}' WHERE {} = '{}';".format(tipo_alteracao, novoValor, tipo_pesquisa, valorIdentificacao)
            try:
                cursor = self.conexao.execute(query)
                cursor = self.conexao.execute("SELECT * FROM medicamentos WHERE {} = '{}'".format(tipo_pesquisa, valorIdentificacao))
                print('Dado(s) alterado(s)..')
                for dados in cursor:
                    print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
            except:
                print("Não foi possível concluir sua solicitação.")
        elif(tipo_pesquisa == "nome" and tipo_alteracao != "nome"):
            query = "UPDATE medicamentos SET {} = '{}' WHERE {} = {};".format(tipo_alteracao, novoValor, tipo_pesquisa, valorIdentificacao)
            try:
                cursor = self.conexao.execute(query)
                cursor = self.conexao.execute("SELECT * FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valorIdentificacao))
                print('Dado(s) alterado(s)..')
                for dados in cursor:
                    print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
            except:
                print("Não foi possível concluir sua solicitação.")
        else:
            query = "UPDATE medicamentos SET {} = {} WHERE {} = {};".format(tipo_alteracao, novoValor, tipo_pesquisa, valorIdentificacao)
            try:
                cursor = self.conexao.execute(query)
                cursor = self.conexao.execute("SELECT * FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valorIdentificacao))
                print('Dado(s) alterado(s)..')
                for dados in cursor:
                    print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
            except:
                 print("Não foi possível concluir sua solicitação.")

    # Exclue uma informação    
    def excluirDado(self, valorIdentificacao, tipo_pesquisa):
        if(tipo_pesquisa == "nome"):
            query = "DELETE FROM medicamentos WHERE {} = '{}'".format(tipo_pesquisa, valorIdentificacao)
            try:
                self.conexao.execute(query)
                print('O(s) dado(s) identificado(s) por {} foram excluido(s).'.format(valorIdentificacao))
            except:
                return print("Não foi possível concluir sua solicitação.")
        else:
            query = "DELETE FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valorIdentificacao)
            try:
                self.conexao.execute(query)
                print('O(s) dado(s) identificado(s) por {} foram excluido(s).'.format(valorIdentificacao))
            except:
                return print("Não foi possível concluir sua solicitação.")
