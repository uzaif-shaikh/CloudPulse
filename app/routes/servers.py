from flask import Blueprint, render_template

servers_bp = Blueprint("servers", __name__)


@servers_bp.route("/servers")
def servers():
    return render_template(
        "servers.html",
        active_page="servers"
    )