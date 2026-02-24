from modules.aluno import Aluno
from modules.mysql import MySQL

banco = MySQL('127.0.0.1', 'root', '', 'universidade')

banco.connect()

aluno = Aluno(
    "Jose Maria",
    "josemaria@gmail.com",
    "98765432110",
    "031985972750",
    "rua paineiras, eldorado, 3000"
    )

query = aluno.cadastrar()
#print(query)

banco.execute_query(query)
banco.disconnect()