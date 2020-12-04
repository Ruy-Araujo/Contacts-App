from contato import Contato
from prettytable import PrettyTable

listaContatos = []

def novoContato():
    nome     = input('Digite um nome para o contato: ')
    email    = input('Digite um email para o contato: ')
    telefone = input('Digite um telefone para o contato: ')
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

def buscaNome(nome):
    resultado = ([contato for contato in listaContatos if contato.nome == nome])
    #tablea = PrettyTable(['Nome','Email','Telefone'])
    tabela = tabelaModelo()
    
    for contato in resultado:
        tabela.add_row([contato.nome,contato.email,contato.telefone])
    print(tabela)

def buscaEmail(email):
    resultado = ([contato for contato in listaContatos if contato.email == email])
    tabela = tabelaModelo()
    for contato in resultado:
        tabela.add_row([contato.nome,contato.email,contato.telefone])
    print(tabela)

def buscaTelefone(email):
    resultado = ([contato for contato in listaContatos if contato.email == email])
    tabela = tabelaModelo()
    for contato in resultado:
        tabela.add_row([contato.nome,contato.email,contato.telefone])
    print(tabela)

#def deletaContato():
