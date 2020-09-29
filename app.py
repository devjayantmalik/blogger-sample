from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if len(email) > 20:
            return {"success": False, "message": "Mujhe bewkoof man rakha kya."}, 400;

        if not email or not password:
            return {"success": False, "message": "Email and Password are required."}, 400;

        return {"email": email, "password": password}


if __name__ == "__main__":
    app.run(debug=True)
