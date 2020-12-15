from agenda import *
import sys,os,time


def limpaTela():
    if sys.platform.startswith('linux'):
        os.system('clear')

    elif sys.platform.startswith('win32'):
        os.system('cls')

def espera(segundos):
    time.sleep(segundos)

def saudacao():
    print('Olá seja bem vindo a agenda de contatos v1.0!\n')

def menuPrincipal():
    opcoes = [
        "Listar contatos",
        "Procurar um contato",
        "Adicionar um novo contato manualmente",
        "Adicionar um novo contato automaticamente",
        "Alterar um contato existente",
        "Remover um contato existente",
        "Sair"
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
    valido = False
    #saudacao()
    while not valido:
        limpaTela()
        opcao = input(menuPrincipal())

    # Lista Contatos
        if opcao == "1":
            limpaTela()
            imprimeContatos()
            espera(5)
        
    # Busca Contato
        elif opcao == "2":
            limpaTela()
            busca = input(menuProcuraContato())
            
            if busca == "1":
                nome = input('\nDigite o nome desejado:\n')
                limpaTela()
                print("Nome buscado: ",nome)
                buscaNome(nome)
                espera(5)

            elif busca == "2":
                email = input('\nDigite o email desejado:\n')
                limpaTela()
                print("Email buscado: ",email)
                buscaEmail(email)
                espera (5)

            elif busca == "3":
                telefone = input('\nDigite o telefone desejado:\n')
                limpaTela()
                print("Tefone buscado: ",telefone)
                buscaTelefone(telefone)
                espera(5)

    # Adicionar Contato Manualmente
        elif opcao == "3":
            limpaTela()
            print('Adicionar novo contato\n')
            nome     = input("Digite o nome do contato: ")
            email    = input("Digite o email do contato: ")
            telefone = input("Digite o telefone do contato: ")
            novoContato(nome,email,telefone)
            espera(3)

    # Adicionar Contato Automaticamente
        elif opcao == "4":
            limpaTela()
            adicionaRandon()
            espera(3)

    # Alterar Contato
        elif opcao == "5":
            limpaTela()
            print("Alterar informações do contato\n")
            email = input("Digite o email do contato: ")
            alteraContato(email)
            espera(3)

    # Remover Contato
        elif opcao == "6":
            limpaTela()
            print("Remover informações do contato\n")
            email = input("Digite o email do contato: ")
            deletaContato(email)
            espera(3)

    # Sair
        elif opcao == "7":
            valido = True
            limpaTela()
            print('Até a proxima!')
            espera(3)
            
    os.system("exit")

main()

