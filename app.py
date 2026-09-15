from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def wecome():
    username = request.form.get("username")
    password = request.form.get("pass")
    if username == "uzaif" and password == "123":
        return redirect(url_for('dashboard'))
    else:
        return "Web site is under devlopment. Now only admin can login."

@app.route('/dashboard')
def dashboard():
    return render_template('project.html', active_page='dashboard')

@app.route('/reports')
def reports():
    return render_template('reports.html', active_page='reports')
@app.route('/servers')
def servers():
    return render_template('servers.html', active_page='servers')

@app.route('/alerts')
def alerts():
    return render_template('alerts.html', active_page='alerts')