

def search_user_path(id: int, userslist: list):
    users = filter(lambda user: user.id == id, userslist)
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado el id {}".format(id)}
    


def search_user_query(id: int,userslist: list):
    users = filter(lambda user: user.id == id, userslist)
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado el id {}".format(id)}
