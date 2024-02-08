# Exercício Banco de Dados

# Importação da biblioteca SQLite3
import sqlite3

# Conectando a um banco de dados
conexao = sqlite3.connect('exercicio_womakerscode')
cursor = conexao.cursor()

# 1.Crie uma tabela chamada "alunos" com os seguintes campos: 
#     id (inteiro), 
#     nome(texto), 
#     idade(inteiro)
#     curso(texto). 

"""cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')"""

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

""" cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Srta. Fernanda Vieira", 28, "Engenharia civil")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Ana Clara Cardoso", 25, "Direito")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Vitor Gabriel da Costa", 22, "Direito")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Levi da Cunha", 20, "Engenharia Civil")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Ana Laura Campos", 28, "Sistemas de Informação")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (6, "Nicole da Cunha", 23, "Medicina")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (7, "Alexandre Pires", 18, "Pedagogia")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (8, "Elisa Aragão", 19, "Enfermagem")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (9, "Bruna Alves", 29, "Sistemas de Informação")')
cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (10, "Samuel Gonçalves", 26, "Psicologia")') """


# 3.Consultas Básicas 
# Escreva consultas SQL para realizar as seguintes tarefas:
# a)Selecionar todos os registros da tabela "alunos".

""" dados_select = cursor.execute('SELECT * FROM alunos')
for alunos in dados_select:
    print(alunos) """

# b)Selecionar o nome e a idade dos alunos com mais de 20 anos. 

""" dados_nome_idade = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for alunos in dados_nome_idade:
    print(alunos) """

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

""" dados_engenharia = cursor.execute('SELECT * FROM alunos WHERE curso LIKE "Engenharia %" ORDER BY 2')
for alunos in dados_engenharia:
    print(alunos) """

# d)Contar o número total de alunos na tabela 

""" cursor.execute('SELECT COUNT(*) FROM alunos')
print("Total de alunos: ", cursor.fetchone()[0]) """

# 4.Atualização e Remoção
# a)Atualize a idade de um aluno específico na tabela. 

""" for aluno in cursor.execute('SELECT * FROM alunos'):
    print(aluno)

cursor.execute('UPDATE alunos SET idade = 25 WHERE id = 6')
print("----------")

for aluno in cursor.execute('SELECT * FROM alunos'):
    print(aluno) """

# b)Remova um aluno pelo seu ID. 

""" cursor.execute('DELETE FROM alunos WHERE id = 10')

for aluno in cursor.execute('SELECT * FROM alunos'):
    print(aluno) """

# 5.Criar uma Tabela e Inserir Dados 
# Crie uma tabela chamada "clientes" com os campos: 
    # id (chave primária)
    # nome(texto), 
    # idade(inteiro)
    # saldo(float)

""" cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT)') """

# Insira alguns registros de clientes na tabela. 

""" cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Ryan Peixoto", 29, 901.60)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Vitor Hugo Farias", 34, 74.99)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Dra. Ana Alves", 63, 55.78)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Evelyn Dias", 28, 510.51)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Stephany Caldeira", 56, 83.91)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (6, "Augusto Gomes", 40, 516.64)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (7, "Maitê Castro", 52, 37.66)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (8, "Theo Cavalcanti", 31, 527.15)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (9, "João Miguel Barbosa", 43, 620.79)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (10, "João Felipe Duarte", 29, 474.44)') """

# 6.Consultas e Funções Agregadas 
# Escreva consultas SQL para realizar as seguintes tarefas:
# a)Selecione o nome e a idade dos clientes com idade superior a 30 anos.

""" for cliente in cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30'):
    print(cliente) """


# b)Calcule o saldo médio dos clientes.

""" media_saldo_clientes = cursor.execute('SELECT AVG(saldo) FROM clientes')
print("O saldo médio dos clientes é: ", round(media_saldo_clientes.fetchone()[0], 2)) """

# c)Encontre o cliente com o saldo máximo.

""" max_saldo_clientes = cursor.execute('SELECT MAX(saldo) FROM clientes')
print("O saldo máximo entre os clientes é: ", max_saldo_clientes.fetchone()[0]) """

#apenas verificando
""" for cliente in cursor.execute('SELECT saldo FROM clientes ORDER BY 1 DESC '):
    print(cliente)
 """

# d)Conte quantos clientes têm saldo acima de 1000.

""" cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo > 1000')
print("Clientes com saldo superior a R$1000: ", cursor.fetchone()[0]) """

# 7.Atualização e Remoção com Condições
# a)Atualize o saldo de um cliente específico.

""" print(cursor.execute('SELECT * FROM clientes WHERE id = 7').fetchone())

cursor.execute('UPDATE clientes SET saldo = 1340.97 WHERE id = 7')

print("-----------------------------------------------------")

print(cursor.execute('SELECT * FROM clientes WHERE id = 7').fetchone()) """

# b)Remova um cliente pelo seu ID.

""" cursor.execute('DELETE FROM clientes WHERE id = 10')

for cliente in cursor.execute('SELECT * FROM clientes'):
    print(cliente) """

# 8.Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: 
    # id (chaveprimária)
    # cliente_id(chave estrangeira referenciando o id da tabela "clientes")
    # produto(texto)
    # valor(real)

""" cursor.execute('CREATE TABLE compras (id INT, id_cliente, produto VARCHAR(100), preco FLOAT)') """

# Insira algumas compras associadas a clientes existentes na tabela "clientes". 

""" cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (1, 7, "Purificador de Ar Difusor", 291.70)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (2, 1, "Ring lights", 198.77)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (3, 8, "Barbeador Bletrico", 314.16)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (4, 7, "Lâmpadas de LED", 148.24)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (5, 2, "Purificador de Ar Difusor", 81.27)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (6, 8, "Fone de Ouvido", 175.90)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (7, 7, "Purificador de Ar Difusor", 88.22)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (8, 5, "Purificador de Ar Difusor", 468.61)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (9, 8, "Caixinhas de som Bluetooth", 339.91)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (10, 1, "Lâmpadas de LED", 353.07)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (11, 3, "Smartwatch", 443.73)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (12, 3, "Barbeador Bletrico", 51.37)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (13, 9, "Barbeador Bletrico", 111.45)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (14, 1, "Barbeador Bletrico", 391.56)')
cursor.execute('INSERT INTO compras (id, id_cliente, produto, preco) VALUES (15, 8, "Fone de Ouvido", 67.48)') """


# Escreva uma consulta para exibir o nome do cliente,o produto e o valor de cada compra.

""" dados_join = cursor.execute('SELECT nome, produto, preco FROM clientes RIGHT JOIN compras ON clientes.id = compras.id_cliente')

for cliente in dados_join:
    print(cliente) """

conexao.commit()
conexao.close