from repository import db_logic
from models import user as us
#Devuelve una lista de objetos(serializados) de la clase usuario

def login():
    #TODO: REVISAR ERRORES 

    #aqui estara el business logic del authentication
    results = db_logic.getAllUsers()
    print(results)
    users = []
    for row in results:
        user = us.User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        print(user.username)
        users.append(user.serialize())
    return users

