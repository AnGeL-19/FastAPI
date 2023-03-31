from typing import Annotated
from fastapi import FastAPI, Query
from database import conexion

# from routes import userroute

from pydantic import BaseModel
import uvicorn



class User(BaseModel):
    id: int
    name: str
    age: int | None = None


app = FastAPI()

db = conexion.SingletonConexionDB()
# app.include_router(userroute, prefix="/book")

users = [
    {
        'id': 1,
        'name': 'John',
        'age': 26
    },
    {
        'id': 2,
        'name': 'Pepe',
        'age': 21
    },
    {
        'id': 3,
        'name': 'Angel',
        'age': 23
    },
]

@app.on_event("startup")
async def startup():
    await db.connect_database()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect_database()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/amonos")
async def amonos(skip:int, limit:int):
    print(skip, limit)
    return {
        "message": "Amonos perro!",
        "skip": skip,
        "limit": limit
        }

@app.get("/user/{user_id}")
async def get_user_by_id(user_id:int):

    user = [user for user in users if user['id'] == int(user_id)][0]

    return {
        "user": user
        }

# @app.get("/users/")
# async def get_users(skip:int = 0, limit:int = 5):

#     list_users = [ users[skip: skip + limit] ]

#     return {
#         "users": list_users
#         }


@app.get("/users/")
async def get_users(q: Annotated[str | None, Query(title="Query string", 
                                                   min_length=3, 
                                                   max_length=50)] = None):

    # list_users = [ users[skip: skip + limit] ]
    print(q)
    # if q:
    #     print(q)
    # else:
    #     print('no esta', q)

    return {
        "users": ''
        }


@app.post("/user")
async def add_user(user: User):

    users.append(user)

    return {
        "user": user
        }

if __name__ == "__main__":

    # only_one_conexion = conexion.SingletonConexionDB()
    # only_one_conexion.conexion_database()
    uvicorn.run("demo:app", host='127.0.0.1', port=8000, reload=True)