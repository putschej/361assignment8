# Jennifer Putsche
# putschej@oregonstate.edu
# CS361 Spring 2025
# S2.6 - Assignment 8: "Microservice A"
# See docs for Flask: https://flask.palletsprojects.com/en/latest/quickstart/

from flask import Flask, request, jsonify
from nba_utils import get_team_roster

app = Flask(__name__)

@app.route("/getTeamRoster", methods=["POST"])
def get_roster():
    data = request.get_json()

    team_abbr = data.get("team name")
    alphabetical = data.get("alphabetical order", False)

    if not team_abbr:
        return jsonify({"valid": False, "results": []}), 400

    result = get_team_roster(team_abbr, alphabetical)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)  # http://127.0.0.1:5000/
