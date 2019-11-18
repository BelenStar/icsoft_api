from flask import Flask
from config import config
from controllers import auth, users
from repository import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config["development"])
db = db.db
db.init_app(app)

#routes
app.register_blueprint(auth.auth_controller)
app.register_blueprint(users.users_controller)


@app.route("/")
def index():
    return auth.hello()

if __name__ == "__main__":
    app.run()
