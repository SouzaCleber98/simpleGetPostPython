# 🌐 Documentação do Módulo: route.py

Este módulo define as rotas do **Flask** para lidar com requisições HTTP `POST` e `GET`.

## 📌 Endpoints definidos:

- `POST /`: Recebe dados do formulário via a função `get_post_data()` do controller.
- `GET /`: Recupera dados do banco de dados via a função `get_db_data()` do controller.

---

## 🔧 Funções:

### `post_response()`

- 📎 Método: `POST`
- 📍 Rota: `'/'`
- 📝 Descrição:  
  Lida com requisições POST à rota raiz.  
  Processa os dados do formulário chamando `get_post_data()` e:
  - Se a operação for bem-sucedida (`status 200`), retorna uma mensagem de sucesso com os dados.
  - Caso contrário, retorna uma mensagem de erro com status `400`.

---

### `get_response()`

- 📎 Método: `GET`
- 📍 Rota: `'/'`
- 📝 Descrição:  
  Lida com requisições GET à rota raiz.  
  Recupera os dados do banco de dados chamando `get_db_data()` e:
  - Se a operação for bem-sucedida (`status 200`), retorna os dados em formato JSON.
  - Em caso de falha, retorna uma mensagem de erro com status `500`.
