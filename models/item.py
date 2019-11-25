from repository import db_logic
from models import errors

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
         "price": str(self.price), "path_to_picture": self.path_to_picture, "provider": self.provider, "quantity": self.quantity}

    @staticmethod
    def getAllItems():
        res = db_logic.getAllItems()
        items = []

        for item in res:
            itemO  = Item(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7])
            items.append(itemO.serialize())
        return items

    @staticmethod
    def getItemById(id):
        res = db_logic.selectItemById(id)
        if len(res) == 0:
            return errors.ItemNotFound()
        row = res[0]
        item = Item(row[0],row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        return item.serialize()
