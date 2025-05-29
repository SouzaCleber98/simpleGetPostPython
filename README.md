# Projeto Flask com PostgreSQL

## Visão Geral

Esta aplicação desenvolvida com **Flask** para receber dados via formulário, inserir esses dados em um banco de dados **PostgreSQL** e retornar o resultado da operação.

---

## Estrutura do Projeto

- `src/controllers/controller.py` — lógica de manipulação e inserção dos dados.
- `src/database/db.py` — conexão com o banco PostgreSQL.
- `src/routes/route.py` — rotas HTTP.
- `.env` — variáveis de ambiente para configuração.
- `requirements.txt` — dependências Python.

---
## Configuração

### Instalação de Dependências

instale as depedencias para usar o projeto

```bash
pip install -r requirements.txt
```

### Variáveis de Ambiente

Renomear o arquivo `.env.exemple` para `.env`
ou
Crie um arquivo `.env` com as variáveis:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASS=senha
```
---

## Funções importantes 

### Controller

 `src/controllers/controller.py` — lógica de manipulação e inserção dos dados.
![Funções controller](assets\imgs\codeController00.png)
- [Funções Controller](assets\functions\functionsController.md)


### Database

`src/database/db.py` — conexão com o banco PostgreSQL.
![Funções database](assets\imgs\codeDatabase00.png)
- [Funções Database](assets\functions\functionsDatabase.md)

### Routes

`src/routes/route.py` — rotas HTTP.
![Funções routes](assets\imgs\codeRoutes00.png)
- [Funções routes](assets\functions\functionsRoutes.md)
Obs: Altere as rotas para o seu uso

---

## Executar a Aplicação

```bash
python -m src.main.app   
```




