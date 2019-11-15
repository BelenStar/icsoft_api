from repository import db_logic
def login():
    #aqui estara el business logic del authentication
    return db_logic.getAllUsers()
