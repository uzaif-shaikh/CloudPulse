from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# 2. Add a secret key (required to encrypt session data)
app.secret_key = "any_random_string_here"

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def wecome():
    username = request.form.get("username")
    password = request.form.get("pass")
    
    if username == "uzaif" and password == "123":
        # 3. Store the username in the session dictionary
        session["user_name"] = username
        return redirect(url_for('dashboard'))
    else:
        return f"Hello! {username} Web site is under devlopment. Now only admin can login."

@app.route('/dashboard')
def dashboard():
    # 4. Retrieve the username from the session (default to "Guest" if not found)
    logged_in_user = session.get("user_name", "Guest")
    
    # 5. Pass it to your project.html template
    return render_template("project.html", usern=logged_in_user)

@app.route('/reports')
def reports():
    return render_template('reports.html', active_page='reports')
@app.route('/servers')
def servers():
    return render_template('servers.html', active_page='servers')

@app.route('/alerts')
def alerts():
    return render_template('alerts.html', active_page='alerts')
@app.route('/settings')
def settings():
    return render_template('settings.html', active_page='settings')

@app.route('/users')
def users():
    return render_template('users.html', active_page='users')
@app.route('/logout')
def logout():
     session.pop('user_name', None) # Removes the user from session
     return redirect(url_for('form'))