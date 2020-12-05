import mysql.connector
   
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

def insereContato():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
        )

    cursor =  conn.cursor()

    lista = [(contato.nome,contato.email,contato.telefone)]
    
    if contato.id_contato:
        cursor.excute("""
        UPDATE contatos 
        SET nome = ?, telefone = ?
        WHERE id = ?
        """,(contato.nome,contato.telefone,contato.id_contato))

    else:
        cursor.execute("""
        INSERT INTO contatos(nome,email,telefone) 
        VALUES(?,?,?)""",lista)
    
    conn.commit()
    print("Dados salvos com sucesso.")
    conn.close()

def procuraContato():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
        )

    cursor =  conn.cursor()

    contatos = []

    cursor.execute(SELECT id,nome,email,telefone FROM contatos)

    for linha in cursor.fetchall():
        contatos.append(Contato(id_contato=linha[0],nome=linha[1],email=linha[2],telefone=linha[3]))
    
    conn.close()
    return contatos

def procuraNome(nome):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
        )

    cursor =  conn.cursor()

    contatos = []

    cursor.execute(SELECT id,nome,email,telefone FROM contatos WHERE nome=?,[nome])

    for linha in cursor.fetchall():
        contatos.append(Contato(id_contato=linha[0],nome=linha[1],email=linha[2],telefone=linha[3]))
    
    conn.close()
    return contatos

def procuraEmail(email):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
        )

    cursor =  conn.cursor()

    contatos = []

    cursor.execute(SELECT id,nome,email,telefone FROM contatos WHERE email=?,[email])

    contato = None

    for linha in cursor.fetchall():
        contato = contatos.append(Contato(id_contato=linha[0],nome=linha[1],email=linha[2],telefone=linha[3]))

    conn.close()
    return contato

def procuraTelefone(telefone):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agenda"
        )

    cursor =  conn.cursor()

    contatos = []

    cursor.execute(SELECT id,nome,email,telefone FROM contatos WHERE telefone=?,[telefone])

    for linha in cursor.fetchall():
        contatos.append(Contato(id_contato=linha[0],nome=linha[1],email=linha[2],telefone=linha[3]))
    
    conn.close()
    return contatos

