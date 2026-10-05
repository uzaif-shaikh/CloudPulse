from flask import Blueprint, render_template


alerts_bp = Blueprint("alerts", __name__)


@alerts_bp.route("/alerts")
def alerts():
    return render_template(
        "alerts.html",
        active_page="alerts"
    )