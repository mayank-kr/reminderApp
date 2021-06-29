# Reminder Application 
# Authors: Sharon, Hailey, Mayank

# import modules
from flask import Flask, redirect, url_for, render_template, request

# app configurations 
app = Flask(__name__)
app.secret_key = "reminder-app"

# home page. reminders are added here 
@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        reminderName = request.form["rname"]
        reminderTime = request.form["time"]
        return redirect(url_for("view",name=reminderName, time=reminderTime))
    return render_template("index.html")

# view reminders page.
@app.route("/view", methods=["POST","GET"])
def view():
    if request.method == "POST":
        return redirect(url_for("home"))
    return render_template("view.html",name=request.args.get("name"),time=request.args.get('time'))

# run the app
if __name__ == "__main__":
    app.run(debug=True)

