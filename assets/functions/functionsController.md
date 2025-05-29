# 📚 Documentação das Funções

## 📥 Função: `get_post_data`

Responsável por receber dados de um formulário enviado via **requisição POST** com Flask, inserir no banco de dados PostgreSQL e retornar o dado inserido.

### 🔁 Processo:
1. Captura o dado do formulário para um campo específico.
2. Se o dado não for fornecido, retorna **HTTP 400** com `None`.
3. Estabelece conexão com o banco via função auxiliar.
4. Prepara e executa a query SQL `INSERT` para inserir o dado na tabela/coluna definida.
5. Executa `commit()` para salvar as alterações.
6. Fecha o cursor e a conexão com o banco corretamente.
7. Retorna **HTTP 200** com os dados inseridos.
8. Em caso de erro, imprime a mensagem no console e retorna **HTTP 500** com `None`.

### 🔄 Retorno:
```python
Tuple[int, Union[dict, None]]
```
- Código HTTP (ex: 200, 400, 500)
- Dado inserido como `dict` se bem-sucedido, ou `None` se houve erro ou dado ausente.

---

## 📤 Função: `get_db_data`

Conecta-se ao banco de dados PostgreSQL e recupera todos os registros de uma tabela específica.

### 🔁 Processo:
1. Estabelece conexão com o banco via função auxiliar.
2. Executa uma query SQL `SELECT` para buscar todos os dados da tabela.
3. Busca todas as linhas retornadas.
4. Fecha o cursor e a conexão.
5. Retorna **HTTP 200** com os dados obtidos.
6. Em caso de erro, imprime a mensagem no console e retorna **HTTP 500** com `None`.

### 🔄 Retorno:
```python
Tuple[int, Union[list, None]]
```
- Código HTTP (ex: 200 ou 500)
- Lista de registros como `list[dict]` se bem-sucedido, ou `None` em caso de erro.
