from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "iv_planner_secret_key"

# -------------------------------
# Dummy users (temporary)
# -------------------------------
users = {
    "student@example.com": {
        "password": "student123",
        "role": "student"
    },
    "college@example.com": {
        "password": "college123",
        "role": "college"
    },
    "provider@example.com": {
        "password": "provider123",
        "role": "provider"
    },
    "admin@example.com": {
        "password": "admin123",
        "role": "admin"
    }
}

# -------------------------------
# Home
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------------
# Login
# -------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users and users[email]["password"] == password:
            session["user"] = email
            session["role"] = users[email]["role"]

            if session["role"] == "student":
                return redirect(url_for("student_dashboard"))
            elif session["role"] == "college":
                return redirect(url_for("college_dashboard"))
            elif session["role"] == "provider":
                return redirect(url_for("provider_dashboard"))
            elif session["role"] == "admin":
                return redirect(url_for("admin_dashboard"))

        return "Invalid email or password"

    return render_template("login.html")

# -------------------------------
# Register (UI only for now)
# -------------------------------
@app.route("/register")
def register():
    return render_template("register.html")

# -------------------------------
# Dashboards
# -------------------------------
@app.route("/student")
def student_dashboard():
    return "<h1>Student Dashboard</h1>"

@app.route("/college")
def college_dashboard():
    return "<h1>College Dashboard</h1>"

@app.route("/provider")
def provider_dashboard():
    return "<h1>Service Provider Dashboard</h1>"

@app.route("/admin")
def admin_dashboard():
    return "<h1>Admin Dashboard</h1>"

# -------------------------------
# Logout
# -------------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -------------------------------
# Run app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
