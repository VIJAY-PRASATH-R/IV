from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "iv_planner_secret_key"

# -------------------------------
# Dummy users
# -------------------------------
users = {
    "student@example.com": {"password": "student123", "role": "student"},
    "college@example.com": {"password": "college123", "role": "college"},
    "provider@example.com": {"password": "provider123", "role": "provider"},
    "admin@example.com": {"password": "admin123", "role": "admin"},
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

            role = session["role"]
            if role == "student":
                return redirect(url_for("student_dashboard"))
            if role == "college":
                return redirect(url_for("college_dashboard"))
            if role == "provider":
                return redirect(url_for("provider_dashboard"))
            if role == "admin":
                return redirect(url_for("admin_dashboard"))

        return "Invalid credentials"

    return render_template("login.html")

# -------------------------------
# Logout
# -------------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -------------------------------
# Dashboards
# -------------------------------
@app.route("/student")
def student_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("student_dashboard.html")


@app.route("/college")
def college_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("college_dashboard.html")


@app.route("/provider")
def provider_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("provider_dashboard.html")


@app.route("/admin")
def admin_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("admin_dashboard.html")

# -------------------------------
# DAY 5 – IV WORKFLOW (UI ONLY)
# -------------------------------

# Provider
@app.route("/provider/add-iv", methods=["GET", "POST"])
def provider_add_iv():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("provider_add_iv.html")


@app.route("/provider/my-ivs")
def provider_my_ivs():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("provider_my_ivs.html")


# College
@app.route("/college/review-ivs")
def college_review_ivs():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("college_review_ivs.html")


# Student
@app.route("/student/browse-ivs")
def student_browse_ivs():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("student_browse_ivs.html")

# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
