from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import asyncpg

app = FastAPI()

# Modelo de dados
class User(BaseModel):
    id: int = None  # O banco gerará o ID automaticamente
    name: str
    description: str = None

@app.on_event("startup")
async def startup():
    global db_pool
    # Atualize o DSN para usar o nome do serviço do Docker ('db') em vez de 'localhost'
    db_pool = await asyncpg.create_pool(dsn="postgresql://daniels:alice223@db:5432/meus_dados")

@app.on_event("shutdown")
async def shutdown():
    await db_pool.close()

# Rota GET: Obter todos os usuários
@app.get("/users", response_model=List[User])
async def get_users():
    async with db_pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM users")
        return [dict(row) for row in rows]

# Rota POST: Criar novo usuário
@app.post("/users", response_model=User)
async def create_user(user: User):
    async with db_pool.acquire() as conn:
        row = await conn.fetchrow(
            "INSERT INTO users (name, description) VALUES ($1, $2) RETURNING *",
            user.name, user.description
        )
        return dict(row)

# Rota PUT: Atualizar usuário existente
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: User):
    async with db_pool.acquire() as conn:
        row = await conn.fetchrow(
            "UPDATE users SET name=$1, description=$2 WHERE id=$3 RETURNING *",
            updated_user.name, updated_user.description, user_id
        )
        if row:
            return dict(row)
        raise HTTPException(status_code=404, detail="User not found.")

# Rota DELETE: Deletar usuário
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    async with db_pool.acquire() as conn:
        result = await conn.execute("DELETE FROM users WHERE id=$1", user_id)
        if result == "DELETE 1":
            return {"message": "User deleted successfully."}
        raise HTTPException(status_code=404, detail="User not found.")

# Rota raiz
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI + asyncpg integration example!"}
