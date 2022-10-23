# -*- coding: utf-8 -*-

from controller.crud import DbManager 
from data.mock import dados_medicamentos


manager = DbManager()

try:
    manager.criarTabela()
    manager.gerarMock(dados_medicamentos)
except:
    pass

opt = 0 # Valor inicial

while(opt != 6):
    print('-'*50)                                                              
    print('''
    [1] Adicionar fármaco
    [2] Consultar estoque
    [3] Consultar preço de fármaco
    [4] Consultar quantidades de um fármaco
    [5] Editar fármaco
    [6] Finalizar programa
    ''')
    print('-'*50)                                                              
    opt = int(input('Qual a sua opção? '))

    if(opt == 1):
        print('Opt = 1')
    elif(opt == 2):
        print('Opt = 2')
    elif(opt == 3):
        print('Opt = 3')
    elif(opt == 4):
        print('Opt = 4')
    elif(opt == 5):
        print('Opt = 5')
    else:
        print('Opcão inválida! ')
    
print('Finalizando.. Até mais! :)')


