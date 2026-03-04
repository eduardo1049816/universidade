from modules.mysql import MySQL
from modules.aluno import Aluno

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem
)


class Listar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        # ===== ESTILO DA TELA DE LISTAGEM =====
        self.janela.setStyleSheet("""
            QWidget {
                background-color: #f4f6f8;
                font-family: Arial;
                font-size: 13px;
            }

            QTableWidget {
                background-color: white;
                border: 1px solid #bdc3c7;
                gridline-color: #e0e0e0;
                selection-background-color: #d6eaf8;
                selection-color: black;
            }

            QHeaderView::section {
                background-color: #2e86de;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }

            QTableWidget::item {
                padding: 6px;
            }

            QTableWidget::item:selected {
                background-color: #aed6f1;
                color: black;
            }

            QPushButton {
                background-color: #27ae60;
                color: white;
                border-radius: 10px;
                padding: 12px;
                margin-top: 12px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1e8449;
            }

            QPushButton:pressed {
                background-color: #186a3b;
            }
        """)
        # ====================================

        # Ajustes visuais (não mudam estrutura)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(30, 30, 30, 30)

        self.configurar_janela()
        self.criar_componentes()
        self.carregar_dados()

    def configurar_janela(self):
        self.janela.setWindowTitle("Listagem de Alunos")

        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.6)
        altura = int(screen.height() * 0.7)

        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)

    def criar_componentes(self):
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Nome", "Email", "CPF", "Telefone", "Matricula"]
        )

        # Melhorias visuais e de usabilidade (seguras)
        self.tabela.setAlternatingRowColors(True)
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabela.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabela.setSortingEnabled(True)
        self.tabela.horizontalHeader().setStretchLastSection(True)

        self.layout.addWidget(self.tabela)

        botao_atualizar = QPushButton("Atualizar")
        self.layout.addWidget(botao_atualizar)

        botao_atualizar.clicked.connect(self.carregar_dados)

    def carregar_dados(self):
        self.banco.connect()
        alunos = Aluno.listar(self.banco)
        self.banco.disconnect()

        self.tabela.setRowCount(len(alunos))

        for linha, aluno in enumerate(alunos):
            self.tabela.setItem(linha, 0, QTableWidgetItem(str(aluno["id"])))
            self.tabela.setItem(linha, 1, QTableWidgetItem(aluno["nome"]))
            self.tabela.setItem(linha, 2, QTableWidgetItem(aluno["email"]))
            self.tabela.setItem(linha, 3, QTableWidgetItem(aluno["cpf"]))
            self.tabela.setItem(linha, 4, QTableWidgetItem(aluno["telefone"]))

            if aluno["matricula"] == True:
                self.tabela.setItem(linha, 5, QTableWidgetItem("True"))
            else:
                self.tabela.setItem(linha, 5, QTableWidgetItem("False"))


