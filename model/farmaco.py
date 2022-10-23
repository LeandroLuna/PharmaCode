class Farmaco:
    "Classe com atributos e métodos do fármaco"
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

    def setPreco(self, preco):
        self.preco = preco
    
    def getPreco(self):
        return self.nome

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade
    
    def getQuantidade(self):
        return self.quantidade
    