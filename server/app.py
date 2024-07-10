from flask import Flask
from models import db, User, Book, Order
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI", "sqlite:///app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return "<h1>Online Bookstore</h1>"

# Add other routes here...

if __name__ == "__main__":
    app.run(port=5555, debug=True)
