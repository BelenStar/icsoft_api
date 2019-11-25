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
def selectItemById():
    res = db.engine.execute(f"SELECT * FROM items_table WHERE id = '{id}'").fetchall()
    return res