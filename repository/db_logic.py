import sys
import os

from .db import db
def getAllUsers():
    res = db.engine.execute("SELECT * FROM users_table").fetchall()
    #TODO: REVISAR ERRORES
    return res
