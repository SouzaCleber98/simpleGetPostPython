from flask import request
from psycopg2.extras import RealDictCursor
from src.database.db import connect_to_db
form = '' 
table = ''  
query = ''

def get_post_data():

    form = 'data' # nome do campo que você deseja obter do formulário
    data = request.form.get(form)  # pega o valor do campo 
    if not data:
        return 400, None
    
    try:
        conn = connect_to_db()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        table = 'public.content'  # nome da tabela que você deseja consultar
        query = f"INSERT INTO {table} (body) VALUES (%s) RETURNING id, body;" # consulta SQL para obter todos os dados da tabela
        cursor.execute(query, (data,)) 
        result = cursor.fetchone()
        conn.commit()  # confirma a transação
        cursor.close()
        conn.close()
        return 200, result
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return 500, None

    
def get_db_data():
    try:
        conn = connect_to_db()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        table = ''  # nome da tabela que você deseja consultar
        query = f"SELECT * FROM {table}" # consulta SQL para obter todos os dados da tabela
        cursor.execute(query)  
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return 200, rows
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return 500, None