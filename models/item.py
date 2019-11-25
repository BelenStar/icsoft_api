from repository import db_logic

class Item():
    #constructor
    def __init__(self, id, name, category, description, price, path_to_picture, provider,quantity):

        self.id = id
        self.name = name
        self.category = category
        self.description =  description
        self.price = price
        self.path_to_picture = path_to_picture
        self.provider = provider
        self.quantity = quantity


    
    def serialize(self):
        return {"id": self.id, "name": self.name, "category": self.category, "description": self.description,
         "price": self.price, "path_to_picture": self.path_to_picture, "provider": self.provider, "quantity": self.quantity}

        