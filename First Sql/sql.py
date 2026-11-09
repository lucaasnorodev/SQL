import mysql.connector

conexao= mysql.connector.connect(
    host='#',
    user='#',
    password='#',
    database='#',
)
cursor = conexao.cursor()
comando = 'SELECT * FROM bcteste.vendas'
cursor.execute(comando)
resultado = cursor.fetchall()

def mostrar_valores():
    comando = 'SELECT * FROM bcteste.vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cont_2 = 0
    for i in resultado:
        tt = resultado[cont_2][0]
        print(f"OPTION: {tt} = {i[1:3]}")
        cont_2 +=1

choice = int(input("[ 1 ] CONSULTAR DADOS \n [ 2 ] ADICIONAR UM PRODUTO \n [ 3 ] ATUALIZAR \n [ 4 ] delete \n> "))

if choice == 1:
#READ
    cont_1 = 0
    for i in resultado:
        print(f"{i}")
        cont_1 +=1

#CREAT
if choice == 2:
    nome_produto = input("Escreva o Produto> ")
    valor = int(input("Digite o valor do produto> "))
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    print("Produto Inserido no Banco de Dados!")
    cursor.execute(comando)
    conexao.commit()

#UPDATE
if choice == 3:
    call = mostrar_valores()
    print(call)
    choice_update = int(input("Selecione a coluna que deseja alterar \n> "))
    choice_update1 = int(input("[ 1 ] PRODUTO \n [ 2 ] VALOR \n > "))
    if choice_update1 == 1:
        produto = input("Escreva o produto que deseja> ")
        id = choice_update
        comando = f'UPDATE vendas SET nome_produto = ("{produto}") WHERE idVendas = ("{id}")'
        cursor.execute(comando)
        conexao.commit()
    if choice_update1 == 2:
            valor = int(input("Digite o valor> "))
            id = choice_update
            comando = f'UPDATE vendas SET valor = ("{valor}") WHERE idVendas = ("{id}")'
            cursor.execute(comando)
            conexao.commit()

#DELETE
if choice == 4:
    choice_delete = int(input("[ 1 ] Deletar Item \n [ 2 ] Delete All \n>"))
#delete all
    if choice_delete == 1:
        mostrar_valores()
        print(mostrar_valores)
        choice_delete = int(input("Digite> "))
        comando = f'DELETE FROM vendas WHERE idVendas =({choice_delete})'
        cursor.execute(comando)
        conexao.commit()
    if choice_delete == 2:
        cont = 0
        while True: #i armazena o intervalo separado
            t = resultado[cont][0]
            print(f"{t}= {cont} ")
            cont+=1
            comando = f'DELETE FROM vendas WHERE idVendas = ({t})'
            cursor.execute(comando)
            conexao.commit()
            if len(resultado) == cont:
                break

#creat
#nome_produto = "PAO"
#valor = 7
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit()

#update


cursor.close()
conexao.close()