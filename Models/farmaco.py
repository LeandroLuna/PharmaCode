class Farmaco():
    "Classe com atributos e métodos do fármaco"

    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

    def setPreco(self, preco):
        self.preco = preco
    
    def getPreco(self):
        return self.preco

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade
    
    def getQuantidade(self):
        return self.quantidade
    
    def getFarmaco(self):
        print(f'Nome: {self.nome}\nPreço: {self.preco}\nQuantidade: {self.quantidade}\n')

