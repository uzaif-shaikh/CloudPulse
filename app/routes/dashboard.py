from flask import Blueprint, render_template, session

from app.models import Metric


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():

    logged_in_user = session.get("user_name", "Guest")

    metrics = Metric.query.order_by(
        Metric.timestamp.desc()
    ).all()

    return render_template(
        "project.html",
        usern=logged_in_user,
        metrics=metrics
    )