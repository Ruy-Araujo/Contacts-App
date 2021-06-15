<h1 align="center">MyContacts App</h1>

<p align="center">An app made in flask to store and manage contacts.</p>


   * [About](#about)
   * [Features](#features)
   * [Getting Started](#getting-started)
      * [Prerequisites](#prerequisites)
      * [Install and Run](#install-and-run)
   * [Technologies](#Technologies)
   * [Autor](#autor)
   * [License](#license)


## About
This is a project created to apply my studies acquired during the semester.

It's an application developed in Python designed to store and manage contacts of multiple users.



## Features

- [x] User registration
- [x] Contact registration
- [x] Contact management
- [ ] Import/Export contacts
- [ ] Search contact

You can see a demo in the link below:

- link

## 🚀 Getting Started

These instructions will allow you to obtain a copy of the project on your local machine for development and testing purposes.

### 📋 Prerequisites

You need to have Python3.6+ installed on your machine

### 🔧 Install and Run

Clone the project
```sh
$ git clone
```

Install the dependencies
```sh
$ cd contacts_app
$ pip install -r requirements.txt
```

generate a secret key
```sh
$ python3
$ import os
$ os.urandom(12).hex
```

Insert the secret key into __init__.py
```py
app.config['SECRET_KEY'] = '->HERE<-'
```

If you want, create a sqlite database with some examples using the db_init()
```sh
$ python3
$ from run_app import db_init
$ db_init()
```

Run the flask app 
```sh
$ python3 run_app.py
```

The application should be up and running at [http://localhost:5000](http://localhost:5000)

## 🛠️ Technologies

* [SQLite](https://www.sqlite.org/)
* [Flask](https://flask.palletsprojects.com/)
* [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
* [WTForms](https://flask-wtf.readthedocs.io/)
* [Bcrypt](https://flask-bcrypt.readthedocs.io/)

## Autor

<a href="https://github.com/Ruy-Araujo">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/53796141?v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Ruy Araujo</b></sub></a> 

[<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100"/>](https://www.linkedin.com/in/ruy-araujo)
[<img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" width="90"/>](https://medium.com/@ruy.araujo)


## 📄 License

This project is under MIT-license - see file [LICENSE.md](https://github.com/usuario/projeto/licenca) for details.


