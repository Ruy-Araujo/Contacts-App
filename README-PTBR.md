# Agenda de Contatos

Uma agenda de contatos desenvolvida em python com o intuito de fixar os conhecimentos em OOP, gerenciamento de ambientes, banco de dados(MySQL) e web services.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **Implantação** para saber como implantar o projeto.

### 📋 Pré-requisitos

Programas necessarios:

```
Python 3.9
MySQL 8.0.22
```

Bibliotecas necessarias: 

```
prettytable 2.0.0
requests 2.25.0
mysql-connector-python 8.0.22
```

### 🔧 Instalação

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Baixe e instale as bibliotecas necessarias através do PIP:

```
pip install prettytable
pip install requests 
pip install mysql-connector-python
```

Instale o MySQL:

```
sudo apt install mysql
```
Crie um banco no MySQL chamado "agenda":

```
CREATE DATABASE agenda
```
Crie as tabelas do banco "agenda":

```
CREATE TABLE contatos(
        id TINYINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        telefone VARCHAR(255)
```
Termine com um exemplo de como obter dados do sistema ou como usá-los para uma pequena demonstração.

## 🛠️ Construído com

* [MySQL](https://www.mysql.com/) - Banco de Dados
* [Prettytable](https://pypi.org/project/prettytable/) - Usado para formatar as tabelas
* [Requests](https://pypi.org/project/requests/) - Usada para solicitar os contos

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Ruy Araujo** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/Ruy-Araujo)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (MIT) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.


