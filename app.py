from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("form.html")
@app.route("/submit",methods = ["GET","POST"])
def wecome():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("pass")
    if username == "uzaif" and password == "123":
        return render_template("project.html") 
    else:
        return "Web site is under devlopment. Now only admin can login."
@app.route('/reports')
def reports():
    return render_template('reports.html')    