from flask import Flask, request, g, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import requests
import json

app = Flask(__name__)
app.secret_key = "AnYtHiNg"
db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def login():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()