from contato import Contato
from prettytable import PrettyTable

listaContatos = []

def novoContato():
    nome     = input('Digite um nome para o contato: ')
    email    = input('Digite um email para o contato: ')
    telefone = input('Digite um telefone para o contato: ')
    email = validaEmail(email)   
    listaContatos.append(Contato(nome,email,telefone))
    imprimeLista()

def tabelaModelo():
    tabela = PrettyTable(['Nome','Email','Telefone'])
    return tabela

def imprimeLista():
    tabela = tabelaModelo()
    for contato in listaContatos:
        tabela.add_row([contato.nome,contato.email,contato.telefone])
    print(tabela)

def validaEmail(email):
    valido = False
    while not valido:
        resultado = buscaEmail(email)
        if resultado:
            print(f'O email "{email}" já está cadastrado')
            email = input('Digite outro email: ')
        else:
            valido = True
    return email

def buscaNome(nome):
    resultado = ([contato for contato in listaContatos if contato.nome == nome])
    #tablea = PrettyTable(['Nome','Email','Telefone'])
    tabela = tabelaModelo()
    
    for contato in resultado:
        tabela.add_row([contato.nome,contato.email,contato.telefone])
    print(tabela)

def buscaEmail(email):
    resultado = ([contato for contato in listaContatos if contato.email == email])
    if not resultado:
        return False
    return resultado[0]

def buscaTelefone(telefone):
    resultado = ([contato for contato in listaContatos if contato.telefone == telefone])
    tabela = tabelaModelo()
    for contato in resultado:
        tabela.add_row([contato.nome,contato.email,contato.telefone])
    print(tabela)

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

"""
novoContato()
novoContato()
novoContato()
alteraContato('m@m')
deletaContato('a@a')
imprimeLista()
"""