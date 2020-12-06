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
    conn,cursor = openConn()
    lista = [contato.nome,contato.email,contato.telefone]
    
    if contato.idContato:
        cursor.excute("""UPDATE contatos SET nome = %s, telefone = %s WHERE id = %s"""
        ,(contato.nome,contato.telefone,contato.idContato))

    else:
        cursor.execute("ALTER TABLE contatos AUTO_INCREMENT = 1")
        cursor.execute("""INSERT INTO contatos(nome,email,telefone) VALUES(%s,%s,%s)""",lista)
    
    conn.commit()
    conn.close()

def listaContatos():
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

def excluiContato(email):
    conn,cursor = openConn()
    cursor.execute("DELETE FROM contatos WHERE email=(%s)",(email,))
    conn.commit()
    conn.close()

def updateContato(contato):
    lista = [contato.nome,contato.telefone,contato.email]
    conn,cursor = openConn()
    cursor.execute("UPDATE contatos SET nome =(%s),telefone = (%s) WHERE email = (%s)"
    ,(contato.nome,contato.telefone,contato.email))
    conn.commit()
    conn.close()