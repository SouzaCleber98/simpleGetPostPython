from dotenv import load_dotenv
import os
import psycopg2 as db

# Carrega variáveis do .env
load_dotenv()

# Retorna uma conexão com o banco de dados PostgreSQ
def connect_to_db():
    return db.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT'),  
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )