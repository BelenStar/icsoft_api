from repository import db_logic

class Item():
    #constructor
    def __init__(self, id, name, category, description, price, pic, provider):

        self.id = id
        self.name = name
        self.category = category
        self.description =  description
        self.price = price
        self.pic = pic
        self.provider = provider


    
    def serialize(self):
        return {"id": self.id, "name": self.name, "category": self.category, "description": self.description,
         "price": self.price, "pic": self.pic, "provider": self.provider}

        