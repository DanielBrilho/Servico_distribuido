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


## Instruções para Configuração e Execução
 **Usando Docker**:
 - Clonar o repositorio:
     ```bash
    git clone https://github.com/DanielBrilho/Servico_distribuido
    cd Servico_distribuido
    ```
   - Execute os contêineres em produção:
     ```bash
     docker-compose -f docker-composeProduction.yml up -d
     ```
## Acessar API
 **Metodos e ferramenta**:

   - Abra seu navegador ou uma ferramenta como Postman e navegue para `http://127.0.0.1:8000`.
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


## Desenvolvedores
Daniel Brilho & João Gomes.

## Imagem no dockerhub
https://hub.docker.com/repository/docker/danielbrilho223/servico_destribuido/general


## Licença

Este projeto está licenciado sob a Licença MIT.
