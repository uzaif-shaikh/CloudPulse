from datetime import datetime

from app.extensions import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<User {self.username}>"


# ==========================================
# Metric Model
# ==========================================

class Metric(db.Model):

    __tablename__ = "metrics"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    server_id = db.Column(
        db.Integer,
        nullable=False
    )

    cpu_usage = db.Column(
        db.Float,
        nullable=False
    )

    memory_usage = db.Column(
        db.Float,
        nullable=False
    )

    disk_usage = db.Column(
        db.Float,
        nullable=False
    )

    network_sent = db.Column(
        db.Float,
        nullable=False
    )

    network_received = db.Column(
        db.Float,
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow
  )

    def __repr__(self):
        return f"<Metric {self.id}>"