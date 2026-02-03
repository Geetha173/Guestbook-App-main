from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage for guestbook entries
entries = []

@app.route("/")
def index():
    return render_template("index.html")  # Homepage with Sign-in form

@app.route("/sign", methods=["POST"])
def sign():
    name = request.form["name"]
    message = request.form["message"]
    entries.append({
        "name": name,
        "message": message,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return redirect(url_for("guestbook"))  # Redirect to Guestbook page

@app.route("/guestbook")
def guestbook():
    return render_template("guestbook.html", entries=entries)  # Show all entries

if __name__ == "__main__":
    app.run(debug=True)
