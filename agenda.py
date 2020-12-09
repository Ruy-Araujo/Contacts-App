from contato import *
from bancoDados import * 
from prettytable import PrettyTable
import json
import requests as r


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
    for contato in listaContatos():
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
    tabela = tabelaModelo()
    contato = procuraEmail(email)
    if procuraEmail(email):
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
    contato = procuraEmail(email)
    if not contato:
        print(f'Não existe nenhum contato cadastrado com o email "{email}"')
    else:    
        nome     = input('Digite um novo nome para o contato: ')
        telefone = input('Digite um novo telefone para o contato: ') 
        contato.nome,contato.telefone = nome,telefone
        updateContato(contato)
        print('Contato alterado com sucesso!')

def deletaContato(email):
    if procuraEmail(email):
        excluiContato(email)
        print('Contato removido com sucesso!')   
    else:
        print(f'Nenhum contato encontrado com o email: "{email}"') 
   
def requestContato():
    response = r.get("https://randomuser.me/api/?nat=br&inc=name,phone,email&noinfo")
    if response.status_code != 200:
        print('Erro ao consumir o serviço de API!',response.status_code)
        return
    else:
        resultado = response.json()
        contato = Contato(nome = '{} {}'.format(resultado['results'][0]['name']['first'],resultado['results'][0]['name']['last']),
        email = resultado['results'][0]['email'],
        telefone = resultado['results'][0]['phone'])
        return contato
        
def adicionaRandon():
    contato = requestContato()    
    while procuraEmail(contato.email):
        contato = requestContato()
    insereContato(contato)
    print('Contato adicionado com sucesso!')    

