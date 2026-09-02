from flask import Blueprint, jsonify, current_app

api_bp = Blueprint("api", __name__)


@api_bp.route("/")
def home():

    return jsonify({
        "service": "NFL Odds Service",
        "status": "running"
    })


@api_bp.route("/api/status")
def status():

    return jsonify({
        "status": "healthy"
    })


@api_bp.route("/api/odds")
def odds():

    return jsonify(
        current_app.cache_service.get_all_odds()
    )


@api_bp.route("/api/odds/<team>")
def team_odds(team):
    return jsonify(
        current_app.cache_service.get_team_odds(team)
    )


@api_bp.route("/api/update", methods=["POST"])
def update():
    result = current_app.update_service.refresh()

    if not result["success"]:
        return jsonify({
            "status": "failed",
            "error": result["error"],
            "records": 0,
        }), 503

    return jsonify({
        "status": "updated",
        "records": result["records"],
        "snapshot_id": result["snapshot_id"],
    })


@api_bp.route("/api/test-sportsbook", methods=["GET"])
def test_sportsbook():
    events = current_app.sportsbook_service.get_nfl_events(
        include_preseason=True
    )

    if not events:
        return jsonify({
            "count": 0,
            "odds": None,
        })

    event = events[0]

    odds = current_app.sportsbook_service.get_event_odds(
        event["id"],
        ["BetMGM", "Caesars"]
    )

    return jsonify({
        "event": event,
        "odds": odds,
    })
