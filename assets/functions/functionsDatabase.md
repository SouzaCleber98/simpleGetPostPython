# 🔌 Documentação da Função: connect_db

## 📄 Descrição

Estabelece uma conexão com o banco de dados **PostgreSQL** usando variáveis de ambiente.

Esta função utiliza o pacote `psycopg2` para abrir uma conexão com o banco de dados PostgreSQL.  
As credenciais de acesso são carregadas a partir de variáveis de ambiente definidas em um arquivo `.env`, garantindo uma configuração segura e flexível.

## 📦 Variáveis de ambiente utilizadas:

- `DB_HOST`: endereço do host do banco de dados  
- `DB_NAME`: nome do banco de dados  
- `DB_PORT`: porta usada para conexão  
- `DB_USER`: nome de usuário  
- `DB_PASSWORD`: senha de acesso  

## ✅ Requisitos:

- Arquivo `.env` com as variáveis configuradas  
- Biblioteca `psycopg2` instalada  
- Biblioteca `python-dotenv` para carregar as variáveis do `.env`

## 💡 Exemplo de uso:

```python
conn = connect_db()
cursor = conn.cursor()
```
