# -*- coding: utf-8 -*-

from Controllers.crud import DbManager
from Models.farmaco import Farmaco
from Data.mock import dados_medicamentos


class Menu():
    def __init__(self):
        self.manager = DbManager()
        self.opt = 0

    def iniciar_aplicacao(self):
        while (self.opt != 7):
            print('-'*50)
            print("[0] Criar tabela\n[1] Adicionar fármaco\n[2] Consultar estoque\n[3] Consultar informações de um fármaco\n[4] Editar fármaco\n[5] Excluir fármaco\n[6] Gerar mock\n[7] Finalizar programa")
            print('-'*50)
            self.opt = int(input('Qual a sua opção? '))
            opc = 0  # Valor inicial

            if (self.opt == 0):
                self.manager.criarTabela()

            elif (self.opt == 1):
                print('-'*50)
                farmaco = Farmaco()
                farmaco.nome = str(input("Insira o nome do fármaco: "))
                farmaco.preco = float(input("Insira o preço do fármaco: "))
                farmaco.quantidade = int(
                    input("Insira a quantidade a ser guardado: "))
                while (opc != 1):
                    print('-'*50)
                    print('Dados informados:')
                    farmaco.getFarmaco()
                    print('Os dados estão corretos?')
                    opc = int(input('[1] Sim\n[2] Não\nSua escolha: '))
                    if (opc == 1):
                        self.manager.inserirDado(farmaco)
                    elif (opc == 2):
                        farmaco.nome = str(input("Insira o nome do fármaco: "))
                        farmaco.preco = float(input("Insira o preço do fármaco: "))
                        farmaco.quantidade = int(
                            input("Insira a quantidade a ser guardado: "))

            elif (self.opt == 2):
                self.manager.listarDados()

            elif (self.opt == 3):
                print('-'*50)
                print(
                    'Informe como deseja pesquisar pelo fármaco:\n[1] ID\n[2] Nome')
                print('-'*50)
                opc_desejada = int(input('Qual a opção desejada? '))
                if (opc_desejada == 1):
                    id = int(input("Informe o ID do item desejado: "))
                    self.manager.buscarDados(id, "id")
                elif (opc_desejada == 2):
                    nome = str(input("Informe o nome do item desejado: "))
                    self.manager.buscarDados(nome, "nome")
                else:
                    print("Opção inválida.. retornando ao menu inicial.")

            elif (self.opt == 4):
                print('-'*50)
                print(
                    'Informe como deseja identificar pelo fármaco:\n[1] ID\n[2] Nome')
                print('-'*50)
                opc_desejada = int(input('Qual a opção desejada? '))
                if (opc_desejada == 1):
                    id = int(input("Informe o ID do item desejado: "))
                    qty_dados = self.manager.buscarDados(id, "id")
                    if (qty_dados >= 1):
                        print('-'*50)
                        print('[1] Nome\n[2] Preço\n[3] Quantidade')
                        print('-'*50)
                        opc_alterar = int(
                            input("Qual informação você quer alterar? "))
                        if (opc_alterar == 1):
                            nome = str(input('Digite o novo nome: '))
                            self.manager.atualizarDados(id, 'id', 'nome', nome)
                        elif (opc_alterar == 2):
                            preco = float(input('Digite o novo preço: '))
                            self.manager.atualizarDados(id, 'id', 'preco', preco)
                        elif (opc_alterar == 3):
                            quantidade = int(input('Digite a nova quantidade: '))
                            self.manager.atualizarDados(
                                id, 'id', 'quantidade', quantidade)
                        else:
                            print("Opção inválida.. retornando ao menu inicial.")
                    else:
                        print(f"Nenhum fármaco cadastrado com o ID = {id}.")
                elif (opc_desejada == 2):
                    nome = str(input("Informe o nome do item desejado: "))
                    qty_dados = self.manager.buscarDados(nome, "nome")
                    if (qty_dados >= 1):
                        print('-'*50)
                        print('[1] Nome\n[2] Preço\n[3] Quantidade')
                        print('-'*50)
                        opc_alterar = int(
                            input("Qual informação você quer alterar?"))

                        if (opc_alterar == 1):
                            nome = str(input('Digite o novo nome: '))
                            self.manager.atualizarDados(nome, 'nome', 'nome', nome)
                        elif (opc_alterar == 2):
                            preco = float(input('Digite o novo preço:'))
                            self.manager.atualizarDados(
                                nome, 'nome', 'preco', preco)
                        elif (opc_alterar == 3):
                            quantidade = str(input('Digite a nova quantidade:'))
                            self.manager.atualizarDados(
                                nome, 'nome', 'quantidade', quantidade)
                        else:
                            print("Opção inválida.. retornando ao menu inicial.")
                    else:
                        print("Opção inválida.. retornando ao menu inicial.")

            elif (self.opt == 5):
                print('-'*50)
                print(
                    '\nInforme como deseja identificar pelo fármaco:\n[1] ID\n[2] Nome')
                print('-'*50)
                opc_desejada = int(input('Qual a opção desejada? '))
                if (opc_desejada == 1):
                    id = int(input("Informe o ID do fármaco que deseja excluir: "))
                    self.manager.excluirDado(id, "id")
                elif (opc_desejada == 2):
                    nome = str(
                        input("Informe o nome do fármaco que deseja excluir: "))
                    self.manager.excluirDado(nome, "nome")
                else:
                    print("Opção inválida.. Retornando ao menu inicial.")

            elif (self.opt == 6):
                self.manager.gerarMock(dados_medicamentos)

            elif (self.opt == 7):
                print('Finalizando.. Até mais! :)')

            else:
                print('Opcão inválida!')
