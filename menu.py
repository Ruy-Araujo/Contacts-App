from agenda import *
import sys
import os

def limpaTela():
    if sys.platform.startswith('linux'):
        os.system('clear')

    elif sys.platform.startswith('win32'):
        os.system('cls')

def saudacao():
    print('Olá seja bem vindo a agenda de contatos v1.0!\n')

def menuPrincipal():
    opcoes = [
        "Listar contatos",
        "Procurar um contato",
        "Adicionar um novo contato manualmente",
        "Adicionar um novo contato automaticamente",
        "Alterar um contato existente",
        "Remover um contato existente"
    ]
    print("Escolha a opção desejada:\n")
    for index,opcao in enumerate(opcoes,start=1):
        print(f'{index} - {opcao}')
    
    return "\n"

def menuProcuraContato():
    print("Escolha a opção de busca desejada:\n")
    opcoes = [
        "Procurar pelo nome do contato",
        "Procurar pelo email do contato",
        "Procurar pelo telefone do contato"
    ]

    for index,opcao in enumerate(opcoes,start=1):
        print(f'{index} - {opcao}')
    
    return "\n"

def main():
    limpaTela()
    saudacao()
    opcao = input(menuPrincipal())

    if opcao == "1":
        imprimeContatos()

    elif opcao == "2":
        limpaTela()
        busca = input(menuProcuraContato())
        
        if busca == "1":
            nome = input('\nDigite o nome desejado:\n')
            limpaTela()
            print("Nome buscado: ",nome)
            buscaNome(nome)

        elif busca == "2":
            email = input('\nDigite o email desejado:\n')
            limpaTela()
            print("Email buscado: ",email)
            buscaEmail(email)

        elif busca == "3":
            telefone = input('\nDigite o telefone desejado:\n')
            limpaTela()
            print("Tefone buscado: ",telefone)
            buscaTelefone(telefone)


main()

