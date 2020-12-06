import mysql.connector
from contato import *

def criaDB():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
        )
    cursor =  conn.cursor()
    cursor.execute("CREATE DATABASE agenda;")    
    conn.close()
    print('O banco de dados foi criado com sucesso!')

def criaTable():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
        )

    cursor =  conn.cursor()

    cursor.execute("""
        CREATE TABLE contatos(
        id TINYINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        telefone VARCHAR(255)
        );""")

    conn.close()
    print('A tabela contatos foi criado com sucesso!')

def openConn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
        )
    cursor =  conn.cursor()

    return conn,cursor

def insereContato(contato):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
        )

    cursor =  conn.cursor()

    lista = [contato.nome,contato.email,contato.telefone]
    
    if contato.idContato:
        cursor.excute("""UPDATE contatos SET nome = %s, telefone = %s WHERE id = %s"""
        ,(contato.nome,contato.telefone,contato.idContato))

    else:
        cursor.execute("""INSERT INTO contatos(nome,email,telefone) VALUES(%s,%s,%s)""",lista)
    
    conn.commit()
    #print("Dados salvos com sucesso.")
    conn.close()

def procuraContato():
    conn,cursor = openConn()
    contatos = []
    cursor.execute("SELECT id,nome,email,telefone FROM contatos")
    
    for linha in cursor.fetchall():
        contatos.append(Contato(idContato=linha[0],nome=linha[1],email=linha[2],telefone=linha[3]))
    conn.close()
    return contatos

def procuraNome(nome):
    conn,cursor = openConn()
    contatos = []
    cursor.execute("SELECT * FROM contatos WHERE nome=(%s)",(nome,))

    for linha in cursor.fetchall():
        print(linha)
        contatos.append(Contato(idContato=linha[0],nome=linha[1],email=linha[2],telefone=linha[3]))
    
    conn.close()
    return contatos

def procuraEmail(email):
    contato = None
    conn,cursor = openConn()
    cursor.execute("SELECT * FROM contatos WHERE email=(%s)",(email,))
    for linha in cursor.fetchall():
        contato = Contato(idContato=linha[0],nome=linha[1],email=linha[2],telefone=linha[3])
    conn.close()
    return contato

def procuraTelefone(telefone):
    conn,cursor = openConn()
    contatos = []
    cursor.execute("SELECT * FROM contatos WHERE telefone=(%s)",(telefone,))
    
    for linha in cursor.fetchall():
        contatos.append(Contato(idContato=linha[0],nome=linha[1],email=linha[2],telefone=linha[3]))
    
    conn.close()
    return contatos

