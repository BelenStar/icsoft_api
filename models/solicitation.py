from repository import db_logic
class Solicitation():

    @staticmethod
    def makeSolicitation(item_id, employee):
        #TODO: check for errors
        res = db_logic.makeSolicitation(item_id, employee)

        row = res[0]
        status = ""
        print("status",row[3])
        #TODO change this to another function
        if row[4] == 1:
            status = "pending"

        output = {"solicitation_id": row[0], "product_id":row[1], "employee_id":row[2], "date_made":row[3],"status":status  }
        return output
