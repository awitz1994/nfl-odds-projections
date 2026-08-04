from flask import Blueprint, jsonify, current_app

api_bp = Blueprint("api", __name__)


@api_bp.route("/api/status")
def status():

    return jsonify({
        "status": "healthy"
    })


@api_bp.route("/api/update", methods=["POST"])
def update():

    current_app.update_service.refresh()

    return jsonify({
        "status": "updated"
    })


@api_bp.route("/api/odds")
def odds():

    return jsonify(
        current_app.cache_service.get_all_odds()
    )