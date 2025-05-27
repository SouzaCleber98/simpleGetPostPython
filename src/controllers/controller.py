from flask import request
from psycopg2.extras import RealDictCursor
from src.database.db import connect_to_db
FORM = 'name' # Substitua pelo nome do campo do formulário que você deseja capturar
TABLE = 'public.guestbook'  # Substitua pelo nome da sua tabela
query = f"SELECT * FROM {TABLE}"

def get_form_data():
    data = request.form.get(FORM)  # pega o valor do campo 'name'
    if data:
        return 200, data
    else:
        return 400, None
    
def get_db_data():
    try:
        conn = connect_to_db()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)  
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return 200, rows
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return 500, None