# Reminder Application 
# Authors: Sharon, Hailey, Mayank

# import modules
from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime, timedelta

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
    currentTime = db.Column(DateTime, default=None) # the time the reminder was made 
    
    def __init__(self, name, rtime, ctime):
        self.reminderName = name
        self.reminderTime = rtime
        self.currentTime = ctime

# home page.
@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("add"))
    return render_template("home.html",reminders=reminders.query.all(),now=datetime.now())

# add reminder page. reminders are added here 
@app.route("/add", methods=["POST","GET"])
def add():
    if request.method == "POST":
        reminderName = request.form["rname"]
        reminderTime = request.form["time"]
        currentTime = datetime.now()
        reminder = reminders(reminderName,reminderTime,currentTime)
        db.session.add(reminder)
        db.session.commit()
        da = request.form["d"]
        ta = request.form["t"]
        return redirect(url_for("view",name=reminderName,time=reminderTime,d=str(da),t=ta))
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

