# Importando SQLite
import sqlite3 as lite

# Criando conexão
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com o banco de dados realizado com sucesso!')
except lite.Error as e:
    print("Erro ao conectar com o banco de dados:", e)


# Tabela de cursos ------------------------------------------

# Criar cursos (Create C)
def criar_cursos(i):
    with con:
        cur = con.cursor() 
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i)   

#criar_cursos(['Python', 'Semanas', 50])

#Ver todos os cursos ( Read R)
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#print (ver_cursos())


# Atualizar os cursos (Update U)
def atualizar_cursos(i):
    with con:
        cur = con.cursor() 
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=?, WHERE id=?"
        cur.execute(query,i)

l = ['Python', 'Duas Semanas', 50.0, 1]



# Deletar os cursos (Delete D)
def deletar_cursos(i):
    with con:
        cur = con.cursor() 
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query,i)

#deletar_cursos([1])

# Tabela de turmas ------------------------------------------

#Criar Turmas (Inserir)
def criar_turmas(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, cursos_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)


#Ver todas as turmas ( Read R)
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

# Atualizar as turmas (Update U)
def atualizar_turmas(i):
    with con:
        cur = con.cursor() 
        query = "UPDATE Turmas SET nome=?, cursos_nome=?, data_inicio=?, WHERE id=?"
        cur.execute(query,i)

# Deletar turma (Delete D)
def deletar_turmas(i):
    with con:
        cur = con.cursor() 
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query,i)


# Tabela Alunos ------------------------------------------

#Criar Alunos (Create C)
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)



#Ver Alunos ( Read R)
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


# Atualizar Alunos (Update U)
def atualizar_alunos(i):
    with con:
        cur = con.cursor() 
        query = "UPDATE Alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, tuma_nome=? WHERE id=?"
        cur.execute(query,i)

# Deletar Alunos (Delete D)
def deletar_alunos(i):
    with con:
        cur = con.cursor() 
        query = "DELETE FROM Alunos WHERE id=?"
        cur.execute(query,i)