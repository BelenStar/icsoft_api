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




