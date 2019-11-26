from repository import db_logic

class Report():
    @staticmethod
    def generateItemsReport():
        res = db_logic.getLastEntrances()
        totalItems = len(res)
        products = []
        for row in res:
            product = {
                "entrance_id":row[0],
                "product_id":row[1],
                "employee_id":row[2],
                "entrance_time":row[3]
            }
            products.append(product)
        output = {"total_entrances": totalItems, "entrances": products}
        return output
