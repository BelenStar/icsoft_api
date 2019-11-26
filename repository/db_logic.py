import sys
import os

from .db import db
def getAllUsers():
    res = db.engine.execute("SELECT * FROM users_table").fetchall()
    #TODO: REVISAR ERRORES
    return res
def selectUserByUsername(username):
    result = db.engine.execute(f"SELECT * FROM users_table WHERE username = '{username}' ").fetchall()
    print("db_logic", result)
    return result
    #TODO: REVISAR
def getAllItems():
    res = db.engine.execute("SELECT * FROM items_table").fetchall()
    return res
def selectItemById(id):
    res = db.engine.execute(f"SELECT * FROM items_table WHERE id = {id}").fetchall()
    return res
def addItem(id,employee):
    res = db.engine.execute(f"UPDATE items_table SET quantity = quantity + 1 WHERE id = {id}")
    #ID does not exist
    if res.rowcount == 0:
        return False
    res = db.engine.execute(f"INSERT INTO entrances_table (product_id, employee_id, entrance_time) VALUES({id},{employee},NOW())")
    if res.rowcount == 0:
        return False
    db.session.commit()
    return True

def getLastEntrances():
    res = db.engine.execute("SELECT * FROM entrances_table WHERE entrance_time >= NOW() - '1 day'::INTERVAL").fetchall()
    print(res)
    return res

def makeSolicitation(item,employee):
    #status 1: pendiente, 2: en proceso, 3: aprobada, 4: finalizada
    res = db.engine.execute(f"INSERT INTO solicitations_table (product_id, employee_id, date, status) VALUES({item},{employee},NOW(),1) RETURNING *").fetchall()
    return res
