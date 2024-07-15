from flask import Flask
from .app import create_app
from .models import db

app = create_app()

# You can add any additional initialization here if needed

if __name__ == "__main__":
    app.run()
