import sys
import os

from .db import db
def getAllUsers():
    res = db.engine.execute("SELECT * FROM users_table").fetchall()
    #TODO: REVISAR ERRORES
    return res
def selectUserByUsername(username):
    result = db.engine.execute(f"SELECT * FROM users_table WHERE username = {username}").fetchall()
    return result 