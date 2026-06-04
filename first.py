from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    message = None

    if request.method =="POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "sernevar@gmail.com" and password == "12345eiei":
            message = "Login Success"
        else:
            message = "email หรือ password ไม่ถูกต้อง"

    return render_template("001.html", message=message)

if __name__=="__main__":
    app.run(debug=True)