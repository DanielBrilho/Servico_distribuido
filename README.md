# Exemplo de Integração FastAPI + asyncpg

Este repositório fornece um exemplo simples de integração do FastAPI com o asyncpg para operações assíncronas no banco de dados. Abaixo, você encontra uma visão geral do código e instruções para executá-lo.

## Funcionalidades

- **Operações CRUD**: Criar, Ler, Atualizar e Excluir usuários.
- **Acesso Assíncrono ao Banco de Dados**: Usa `asyncpg` para interações assíncronas eficientes com PostgreSQL.
- **Compatível com Docker**: Projetado para funcionar perfeitamente com Docker.

## Endpoints

### 1. Obter Todos os Usuários
**GET** `/users`
- **Descrição**: Retorna uma lista de todos os usuários.
- **Resposta**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "description": "Um usuário de exemplo."
    }
  ]
  ```

### 2. Criar um Usuário
**POST** `/users`
- **Descrição**: Cria um novo usuário.
- **Corpo da Requisição**:
  ```json
  {
    "name": "Jane Doe",
    "description": "Outro usuário de exemplo."
  }
  ```
- **Resposta**:
  ```json
  {
    "id": 2,
    "name": "Jane Doe",
    "description": "Outro usuário de exemplo."
  }
  ```

### 3. Atualizar um Usuário
**PUT** `/users/{user_id}`
- **Descrição**: Atualiza os detalhes de um usuário existente.
- **Corpo da Requisição**:
  ```json
  {
    "name": "Nome Atualizado",
    "description": "Descrição Atualizada."
  }
  ```
- **Resposta**:
  ```json
  {
    "id": 1,
    "name": "Nome Atualizado",
    "description": "Descrição Atualizada."
  }
  ```

### 4. Excluir um Usuário
**DELETE** `/users/{user_id}`
- **Descrição**: Exclui um usuário pelo ID.
- **Resposta**:
  ```json
  {
    "message": "Usuário excluído com sucesso."
  }
  ```

### 5. Endpoint Raiz
**GET** `/`
- **Descrição**: Uma mensagem de boas-vindas para a API.
- **Resposta**:
  ```json
  {
    "message": "Bem-vindo ao exemplo de integração FastAPI + asyncpg!"
  }
  ```

## Requisitos

- Python 3.9+
- Banco de Dados PostgreSQL
- Docker (opcional, mas recomendado)

## Instruções para Configuração e Execução

1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/DanielBrilho/Servico_distribuido
   cd Servico_distribuido
   ```

2. **Instalar Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Preparar o Banco de Dados**:
   - Crie um banco de dados PostgreSQL chamado `meus_dados`.
   - Configure um usuário com o nome `daniels` e a senha `alice223`.
   - Crie uma tabela `users`:
     ```sql
     CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       description TEXT
     );
     ```

4. **Executar a Aplicação**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Acessar a API**:
   - Abra seu navegador ou uma ferramenta como Postman e navegue para `http://127.0.0.1:8000`.

6. **Usando Docker**:
   - Construir a imagem Docker:
     ```bash
     docker build -t fastapi-asyncpg-app .
     ```
   - Executar os contêineres:
     ```bash
     docker-compose up
     ```

## Estrutura do Projeto

```
|---api/
|----Dockerfile
|----requirements.txt
|----main.py
|---db/
|----init.sql
|---docker-compose.yml
```

## Imagem no dockerhub
https://hub.docker.com/repository/docker/danielbrilho223/servico_destribuido/general

## Contribuição

Fique à vontade para abrir issues ou enviar pull requests com melhorias ou correções de bugs.

## Licença

Este projeto está licenciado sob a Licença MIT.

