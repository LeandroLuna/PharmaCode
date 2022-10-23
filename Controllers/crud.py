import sqlite3  
from Models.farmaco import Farmaco

class DbManager():
    # Classe para gerenciar os métodos do banco de dados.
    def __init__(self):
        self.conexao = sqlite3.connect("database.dp")

    # Cria uma tabela.
    def criarTabela(self):
        try:
            self.conexao.execute('''CREATE TABLE medicamentos(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL ,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL);
            ''')
        except:
            print('Já existe uma tabela criada.')
 
    # Insere um dado.
    def inserirDado(self, farmaco: Farmaco):
        query = "INSERT INTO medicamentos (nome, preco, quantidade) VALUES('{}', {}, {});".format(farmaco.getNome(), farmaco.getPreco(), farmaco.getQuantidade())
        self.conexao.execute(query)
        self.conexao.commit()
        
    # Injeta dados mockados.
    def gerarMock(self, dados):
        try:
            for dado in dados:
                self.conexao.execute(dado)
                self.conexao.commit()
        except:
            print('Houve um problema ao inserir os novos dados de teste..')

    # Recupera dados especificos.
    def buscarDados(self, valor, tipo_pesquisa):
        if(tipo_pesquisa == "nome"):
            query = "SELECT * FROM medicamentos WHERE {} = '{}'".format(tipo_pesquisa, valor)
            cursor = self.conexao.execute(query)
            print('-'*50)                                                              
            print(f"Lista dos itens encontrados com {tipo_pesquisa} = '{valor}':\n")
            for dados in cursor:
                    print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
            return cursor.arraysize
        else:
            query = "SELECT * FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valor)
            cursor = self.conexao.execute(query)
            print('-'*50)                                                              
            print(f"Lista dos itens encontrados com {tipo_pesquisa} = '{valor}':\n")
            for dados in cursor:
                    print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
            return cursor.arraysize
            
    # Atualiza as informações dos dados. 
    def atualizarDados(self, valorIdentificacao, tipo_pesquisa, tipo_alteracao, novoValor):
        if(tipo_pesquisa == "nome" and tipo_alteracao == "nome"):
            query = "UPDATE medicamentos SET {} = '{}' WHERE {} = '{}';".format(tipo_alteracao, novoValor, tipo_pesquisa, valorIdentificacao)
            print(query)
            try:
                cursor = self.conexao.execute(query)
                cursor = self.conexao.execute("SELECT * FROM medicamentos WHERE {} = '{}'".format(tipo_pesquisa, valorIdentificacao))
                self.conexao.commit()
                print('Dado(s) alterado(s)..')
                for dados in cursor:
                    print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
            except:
                print("Não foi possível concluir sua solicitação.")
        elif(tipo_pesquisa == "nome" and tipo_alteracao != "nome"):
            query = "UPDATE medicamentos SET {} = {} WHERE {} = '{}';".format(tipo_alteracao, novoValor, tipo_pesquisa, valorIdentificacao)
            print(query)
            try:
                cursor = self.conexao.execute(query)
                cursor = self.conexao.execute("SELECT * FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valorIdentificacao))
                self.conexao.commit()
                print('Dado(s) alterado(s)..')
                for dados in cursor:
                    print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
            except:
                print("Não foi possível concluir sua solicitação.")
        elif(tipo_pesquisa != "nome" and tipo_alteracao == "nome"):
            query = "UPDATE medicamentos SET {} = '{}' WHERE {} = {};".format(tipo_alteracao, novoValor, tipo_pesquisa, valorIdentificacao)
            print(query)
            try:
                cursor = self.conexao.execute(query)
                cursor = self.conexao.execute("SELECT * FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valorIdentificacao))
                self.conexao.commit()
                print('Dado(s) alterado(s)..')
                for dados in cursor:
                    print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
            except:
                print("Não foi possível concluir sua solicitação.")
        else:
            query = "UPDATE medicamentos SET {} = {} WHERE {} = {};".format(tipo_alteracao, novoValor, tipo_pesquisa, valorIdentificacao)
            print(query)
            try:
                cursor = self.conexao.execute(query)
                cursor = self.conexao.execute("SELECT * FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valorIdentificacao))
                self.conexao.commit()
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
                self.conexao.commit()
                print('O(s) dado(s) identificado(s) pelo nome "{}" foram excluido(s).'.format(valorIdentificacao))
            except:
                print("Não foi possível concluir sua solicitação.")
        else:
            query = "DELETE FROM medicamentos WHERE {} = {}".format(tipo_pesquisa, valorIdentificacao)
            try:
                self.conexao.execute(query)
                self.conexao.commit()
                print('O(s) dado(s) identificado(s) pelo id = "{}" foram excluido(s).'.format(valorIdentificacao))
            except:
                print("Não foi possível concluir sua solicitação.")
    
    # Recupera todas informações registradas.
    def listarDados(self):
        query = "SELECT * FROM medicamentos"
        cursor = self.conexao.execute(query)
        for dados in cursor:
            print(f'ID: {dados[0]}\nNome: {dados[1]}\nPreço: {dados[2]}\nQuantidade: {dados[3]}\n')
        
