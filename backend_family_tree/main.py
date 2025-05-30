from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #pozwala wszystkim domenom (na start OK)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    id: int
    login: str
    password: str
    role: str
    created_at: str

db = []

@app.get("/")
def root():
    return {"message": "main page"}


@app.get("/users")
def get_users():
    return db

@app.post("/users")
def create_user(user: User):
    db.append(user)
    return user

@app.put("/users/{id}")
def update_user(id: int, user: User):
    for i, user in enumerate(db):
        if user.id == id:
            db[i] = user
            return user
    return {"error": "user not found"}

@app.delete("/users/{id}")
def delete_user(id: int):
    global db
    db = [u for u in db if u.id != id]
    return {"ok": True}

class Person(BaseModel):
    id: int
    imie: str
    nazwisko: str
    nazwisko_panienskie: str
    data_urodzenia: str
    miejsce_urodzenia: str
    data_smierci: str

@app.get("/people")
def get_people():
    return db

@app.post("/people")
def create_person(person: Person):
    db.append(person)
    return db

