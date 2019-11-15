import sys
import os

from .db import db
def getAllUsers():
    res = db.engine.execute("SELECT * FROM users_table").fetchall()
    for row in res:
        print(res[0])
    return {"username":"admin"}
