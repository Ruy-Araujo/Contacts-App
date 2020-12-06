from contato import *
from bancoDados import * 
from prettytable import PrettyTable

listaContatos = []

def novoContato():
    nome     = input('Digite um nome para o contato: ')
    email    = input('Digite um email para o contato: ')
    telefone = input('Digite um telefone para o contato: ')
    email = validaEmail(email)   
    insereContato(Contato(nome,email,telefone))
    print('Contato adicionado com sucesso!')

def tabelaModelo():
    tabela = PrettyTable(['Nome','Email','Telefone'])
    return tabela

def imprimeContatos():
    tabela = tabelaModelo()
    for contato in procuraContato():
        tabela.add_row([contato.nome,contato.email,contato.telefone])
    print(tabela)

def validaEmail(email):
    valido = False
    while not valido:
        if procuraEmail(email):
            print(f'O email "{email}" já está cadastrado')
            email = input('Digite outro email: ')
        else:
            valido = True
    return email

def buscaNome(nome):
    tabela = tabelaModelo()
    if procuraNome(nome):
        for contato in procuraNome(nome):
            tabela.add_row([contato.nome,contato.email,contato.telefone])
        print(tabela)
    else:
        print(f'Nenhum contato encontrado com o nome: "{nome}"')

def buscaEmail(email):
    resultado = procuraEmail(email)
    tabela = tabelaModelo()
    if resultado:
        for linha in resultado:
            tabela.add_row([contato.nome,contato.email,contato.telefone])
        print(tabela)
    else:
        print(f'Nenhum contato encontrado com o email: "{email}"')

def buscaTelefone(telefone):
    tabela = tabelaModelo()
    if procuraTelefone(telefone):
        for contato in procuraTelefone(telefone):
            tabela.add_row([contato.nome,contato.email,contato.telefone])
        print(tabela)
    else:
        print(f'Nenhum contato encontrado com o telefone: "{telefone}"')

def alteraContato(email):
    contato = buscaEmail(email)
    if not contato:
        print(f'Não existe nenhum contato cadastrado com o email "{email}"')
        return
    nome     = input('Digite um novo nome para o contato: ')
    telefone = input('Digite um novo telefone para o contato: ') 
    contato.nome,contato.telefone = nome,telefone

def deletaContato(email):
    contato = buscaEmail(email)
    if not contato:
        print(f'Não existe nenhum contato cadastrado com o email "{email}"')
        return

    listaContatos.remove(contato)


#novoContato()
#novoContato()
#novoContato()
#alteraContato('m@m')
#deletaContato('a@a')
#imprimeContatos()
#buscaNome('Joseee')
#buscaEmail('jose@email.cm')
#buscaTelefone('11 1111-1111')