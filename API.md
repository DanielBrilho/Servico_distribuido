# Integração FastAPI + asyncpg

Este repositório fornece um exemplo simples de integração do FastAPI com o asyncpg para operações assíncronas no banco de dados. Abaixo, você encontra uma visão geral do código e instruções para executá-lo.
Foi feito para a unidade curricular de sistemas distribuidos no curso de TPSI no IPVC com o Docente Wenderson Wanzeller.

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

