from modules.mysql import MySQL
from modules.aluno import Aluno

import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)

def cadastro():
    aluno = Aluno(
        campo_nome.text(),
        campo_email.text(),
        campo_cpf.text(),
        campo_telefone.text(),
        campo_endereco.text()
    )
    
    banco = MySQL()
    banco.connect()
    
    aluno.cadastrar(banco)
    
    banco.disconnect()

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Cadastro Aluno")
janela.resize(1200, 600)

layoute = QVBoxLayout()

#Componentes
label_nome = QLabel("Digite seu nome: ")
campo_nome = QLineEdit()

label_email = QLabel("Digite seu email: ")
campo_email = QLineEdit()

label_cpf = QLabel("Digite seu cpf: ")
campo_cpf = QLineEdit()

label_telefone = QLabel("Digite seu telefone: ")
campo_telefone = QLineEdit()

label_endereco = QLabel("Digite seu endereço: ")
campo_endereco = QLineEdit()

botao = QPushButton("cadastrar")

# Adicionar componentes a janela
layoute.addWidget(label_nome)
layoute.addWidget(campo_nome)

layoute.addWidget(label_email)
layoute.addWidget(campo_email)

layoute.addWidget(label_cpf)
layoute.addWidget(campo_cpf)

layoute.addWidget(label_telefone)
layoute.addWidget(campo_telefone)

layoute.addWidget(label_endereco)
layoute.addWidget(campo_endereco)

layoute.addWidget(botao)

janela.setLayout(layoute)

botao.clicked.connect(cadastro)

janela.show()
sys.exit(app.exec())