from fastapi import FastAPI

app = FastAPI()

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

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/amonos")
async def amonos():
    return {"message": "Amonos perro!"}


@app.get("/users")
async def amonos():
    return {
        "users": users
        }

@app.get("/users/{user_id}")
async def amonos(user_id:int):

    user = [user for user in users if user['id'] == int(user_id)][0]

    return {
        "user": user
        }