from flask import Blueprint, render_template
from app.models import Metric

servers_bp = Blueprint("servers", __name__)


@servers_bp.route("/servers/")
def servers():

    metrics = Metric.query.order_by(
        Metric.timestamp.desc()
    ).all()

    return render_template(
        "servers.html",
        metrics=metrics
    )