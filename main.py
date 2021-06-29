from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
# from flask.signals import Namespace
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "reminder-app"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.permanent_session_lifetime = timedelta(day=1)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

