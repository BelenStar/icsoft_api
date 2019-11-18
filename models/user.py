from repository import db_logic

class User():
    """constructor"""
    def __init__(self,id,name,lastname,department,username,password,email):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.department = department
        self.username = username
        self.password = password
        self.email = email

    #Devuelve el objeto como diccionario
    def serialize(self):
        return {"id": self.id, "name": self.name, "lastname": self.lastname, "department": self.department,
         "username": self.username, "email": self.email}

    @staticmethod
    def getAllUsers():

        results = db_logic.getAllUsers()
        users = []

        for row in results:
            user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            print(user.username)
            users.append(user.serialize())
        return users
