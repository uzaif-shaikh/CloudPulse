from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models import User


auth_bp = Blueprint("auth", __name__)


# =============================
# LOGIN PAGE
# =============================

@auth_bp.route("/")
def login():

    return render_template("form.html")


# =============================
# LOGIN
# =============================

@auth_bp.route("/submit", methods=["POST"])
def submit_login():

    username = request.form.get("username", "").strip()
    password = request.form.get("pass", "")

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):

        session["user_id"] = user.id
        session["user_name"] = user.username

        return redirect(url_for("dashboard.dashboard"))

    flash(
        "Invalid username or password. Try again.",
        "error"
    )

    return redirect(url_for("auth.login"))


# =============================
# REGISTRATION
# =============================

@auth_bp.route("/register", methods=["POST"])
def register():

    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    # Check empty fields
    if not username or not email or not password:

        flash(
            "All fields are required.",
            "error"
        )

        return redirect(url_for("auth.login"))


    # Check existing username
    existing_username = User.query.filter_by(
        username=username
    ).first()

    if existing_username:

        flash(
            "Username already exists.",
            "error"
        )

        return redirect(url_for("auth.login"))


    # Check existing email
    existing_email = User.query.filter_by(
        email=email
    ).first()

    if existing_email:

        flash(
            "Email already registered.",
            "error"
        )

        return redirect(url_for("auth.login"))


    # Hash password
    password_hash = generate_password_hash(password)


    # Create user
    new_user = User(
        username=username,
        email=email,
        password_hash=password_hash
    )


    # Save to database
    db.session.add(new_user)
    db.session.commit()


    flash(
        "Registration successful. You can now login.",
        "success"
    )

    return redirect(url_for("auth.login"))


# =============================
# LOGOUT
# =============================

@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))