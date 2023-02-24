from fastapi import FastAPI
from pydantic import BaseModel
from function import *

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int
    secretIdentity : str
    powers : str

userslist = [User(id=1,name="Alex",age= 27,secretIdentity= "SuperNigga", powers="High" ),
                User(id=2,name="Brayhan",age= 26,secretIdentity= "Nigga", powers="High" ),
                User(id=3,name="Zuluaga",age= 25,secretIdentity= "Black", powers="Low" ),
                User(id=4,name="Arroyo",age= 28,secretIdentity= "White", powers="Low" )]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Alex", "age": 27, "secretIdentity": "SuperNigga","powers": "High"},
            {"name": "Brayhan", "age": 26, "secretIdentity": "Nigga","powers": "High"},
            {"name": "Zuluaga", "age": 25, "secretIdentity": "Black","powers": "low"}]

@app.get("/users")
async def users():
    return userslist


#Busca id por path
@app.get("/user/{id}")
async def user(id: int):
    return search_user_path(id,userslist)
    

#Busca id por query 
@app.get("/userquery/")
async def userquery(id: int):
    return search_user_query(id,userslist)

@app.post("/user/")
async def user(user: User):
    if search_user_path(user.id, userslist) in userslist:
        return ("El usuario {} ya existe".format(user.id))
    else:
        userslist.append(user)
        return ("El ususario {} se creo correctamente".format(user.id))

@app.put("/user/")
async def user(user: User):
    if not search_user_path(user.id, userslist) in userslist:
        return ("El usuario {} no existe".format(user.id))
    else:
        for index, saved_user in enumerate(userslist):
            if saved_user.id == user.id:
                userslist[index]= user
                return ("El ususario {} se actualizo coreectamente".format(user.id))


@app.delete("/user/{id}")
async def user(id: int):
    found =False
    for index, saved_user in enumerate(userslist):
        if saved_user.id == id:
            del userslist[index]
            found= True
            return ("El usuario {}  ha sido eliminado correctamente".format(id))
    if not found:
        return ("El usuario {} no existe".format(id))