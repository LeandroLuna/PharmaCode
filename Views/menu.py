# -*- coding: utf-8 -*-

import sys
sys.path.append('/Users/leandroluna/Documents/Github/PharmaCode')

from Controllers.crud import DbManager
from Models.farmaco import Farmaco
# from Data.mock import dados_medicamentos

manager = DbManager()

try:
    manager.criarTabela()
#    manager.gerarMock(dados_medicamentos)
except:
    pass

opt = 0  # Valor inicial

while (opt != 6):
    print('-'*50)
    print("[1] Adicionar fármaco\n[2] Consultar estoque\n[3] Consultar informações de um fármaco\n[4] Editar fármaco\n[5] Excluir fármaco\n[6] Finalizar programa")
    print('-'*50)
    opt = int(input('Qual a sua opção? '))
    opc = 0 # Valor inicial 
    
    if (opt == 1):
        print('-'*50)
        farmaco = Farmaco()
        farmaco.setNome(str(input("Insira o nome do fármaco: ")))
        farmaco.setPreco(float(input("Insira o preço do fármaco: ")))
        farmaco.setQuantidade(int(input("Insira a quantidade a ser guardado: ")))
        while(opc != 1): 
            print('-'*50)
            farmaco.getFarmaco()
            print('Os dados estão corretos?')
            opc = int(input('[1] Sim\n[2] Não\nSua escolha: '))
            if(opc == 1):
                manager.inserirDado(farmaco)
            elif(opc == 2):
                farmaco.setNome(str(input("\nInsira o nome do fármaco: ")))
                farmaco.setPreco(float(input("Insira o preço do fármaco: ")))
                farmaco.setQuantidade(int(input("Insira a quantidade a ser guardado: ")))
            
    elif (opt == 2):
        manager.listarDados()

    elif (opt == 3):
        print('-'*50)
        print('Informe como deseja pesquisar pelo fármaco:\n[1] ID\n[2] Nome')
        print('-'*50)
        opc_desejada = int(input('Qual a opção desejada? '))
        if (opc_desejada == 1):
            id = int(input("Informe o ID do item desejado: "))
            manager.buscarDados(id, "id")
        elif (opc_desejada == 2):
            nome = str(input("Informe o nome do item desejado: "))
            manager.buscarDados(nome, "nome")
        else:
            print("Opção inválida.. retornando ao menu inicial.")

    elif (opt == 4):
        print('-'*50)
        print('Informe como deseja identificar pelo fármaco:\n[1] ID\n[2] Nome')
        print('-'*50)
        opc_desejada = int(input('Qual a opção desejada? '))
        if (opc_desejada == 1):
            id = int(input("Informe o ID do item desejado: "))
            qty_dados = manager.buscarDados(id, "id")
            if (qty_dados >= 1):
                print('-'*50)
                print('[1] Nome\n[2] Preço\n[3] Quantidade')
                print('-'*50)
                opc_alterar = int(input("Qual informação você quer alterar? "))
                if (opc_alterar == 1):
                    nome = str(input('Digite o novo nome: '))
                    manager.atualizarDados(id, 'id', 'nome', nome)
                elif (opc_alterar == 2):
                    preco = float(input('Digite o novo preço: '))
                    manager.atualizarDados(id, 'id', 'preco', preco)
                elif (opc_alterar == 3):
                    quantidade = int(input('Digite a nova quantidade: '))
                    manager.atualizarDados(id, 'id', 'quantidade', quantidade)
                else:
                    print("Opção inválida.. retornando ao menu inicial.")
            else:
                print(f"Nenhum fármaco cadastrado com o ID = {id}.")
        elif (opc_desejada == 2):
            nome = str(input("Informe o nome do item desejado: "))
            qty_dados = manager.buscarDados(nome, "nome")
            if (qty_dados >= 1):
                print('-'*50)
                print('[1] Nome\n[2] Preço\n[3] Quantidade')
                print('-'*50)
                opc_alterar = int(input("Qual informação você quer alterar?"))

                if (opc_alterar == 1):
                    nome = str(input('Digite o novo nome: '))
                    manager.atualizarDados(nome, 'nome', 'nome', nome)
                elif (opc_alterar == 2):
                    preco = float(input('Digite o novo preço:'))
                    manager.atualizarDados(nome, 'nome', 'preco', preco)
                elif (opc_alterar == 3):
                    quantidade = str(input('Digite a nova quantidade:'))
                    manager.atualizarDados(nome, 'nome', 'quantidade', quantidade)
                else:
                    print("Opção inválida.. retornando ao menu inicial.")
            else:
                print("Opção inválida.. retornando ao menu inicial.")

    elif (opt == 5):
        print('-'*50)
        print(
            '\nInforme como deseja identificar pelo fármaco:\n[1] ID\n[2] Nome')
        print('-'*50)
        opc_desejada = int(input('Qual a opção desejada? '))
        if (opc_desejada == 1):
            id = int(input("Informe o ID do fármaco que deseja excluir: "))
            manager.excluirDado(id, "id")
        elif (opc_desejada == 2):
            nome = str(input("Informe o nome do fármaco que deseja excluir: "))
            manager.excluirDado(nome, "nome")
        else:
            print("Opção inválida.. Retornando ao menu inicial.")

    elif (opt == 6):
        print('Finalizando.. Até mais! :)')

    else:
        print('Opcão inválida!')