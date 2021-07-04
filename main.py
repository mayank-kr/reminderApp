# Reminder Application 
# Authors: Sharon, Hailey, Mayank

# import modules
from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime

# app configurations 
app = Flask(__name__)
app.secret_key = "reminder-app"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class reminders(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    reminderName = db.Column("name",db.String(100))
    reminderTime = db.Column("time",db.String(100)) # the time to be reminded
    remindAt = db.Column(DateTime, default=None) # the time the reminder was made 
    
    def __init__(self, name, rtime, time):
        self.reminderName = name
        self.reminderTime = rtime
        self.remindAt = time

# home page.
@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("add"))
    return render_template("home.html",reminders=reminders.query.all())

# add reminder page. reminders are added here 
@app.route("/add", methods=["POST","GET"])
def add():
    if request.method == "POST":
        reminderName = request.form["rname"]
        d = request.form["d"]
        t = request.form["t"]
        dt = d + ' ' + t
        remindAt = datetime.strptime(dt, "%Y-%m-%d %H:%M")
        reminder = reminders(reminderName,dt,remindAt)
        db.session.add(reminder)
        db.session.commit()
        return redirect(url_for("view",name=reminderName,time=str(remindAt)))
    return render_template("add.html")

# view reminders page.
@app.route("/view", methods=["POST","GET"])
def view():
    if request.method == "POST":
        return redirect(url_for("home"))
    return render_template("view.html",name=request.args.get("name"),time=request.args.get('time'))

# run the app
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

