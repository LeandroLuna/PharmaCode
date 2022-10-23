class Farmaco():
    "Classe com atributos e métodos do fármaco"

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
        
    def getFarmaco(self):
        print(f'Nome: {self.__nome}\nPreço: {self.__preco}\nQuantidade: {self.__quantidade}\n')

