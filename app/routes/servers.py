from flask import Blueprint, render_template
from app.models import Metric
from flask import request, jsonify
from datetime import datetime
from app.extensions import db

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

@servers_bp.route("/api/metrics", methods=["POST"])
def receive_metrics():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    required_fields = [
        "server_id",
        "cpu_usage",
        "memory_usage",
        "disk_usage",
        "network_sent",
        "network_received",
    ]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        metric = Metric(
            server_id=int(data["server_id"]),
            cpu_usage=float(data["cpu_usage"]),
            memory_usage=float(data["memory_usage"]),
            disk_usage=float(data["disk_usage"]),
            network_sent=float(data["network_sent"]),
            network_received=float(data["network_received"]),
            timestamp=datetime.utcnow(),
        )

        db.session.add(metric)
        db.session.commit()

        return jsonify({
            "message": "Metrics saved successfully",
            "id": metric.id,
        }), 201

    except (ValueError, TypeError):
        db.session.rollback()
        return jsonify({"error": "Invalid metric values"}), 400

    except Exception:
        db.session.rollback()
        return jsonify({"error": "Could not save metrics"}), 500
