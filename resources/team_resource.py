from flask import request
from flask_restx import Namespace, Resource, fields
from services.team_service import fetch_team_data

ns = Namespace("teams", description="Team operations")

# Define expected output model
team_model = ns.model(
    "Team",
    {
        "idTeam": fields.String(example="133604"),
        "strTeam": fields.String(example="Bayern Munich"),
        "strLeague": fields.String(example="German Bundesliga"),
        "intFormedYear": fields.String(example="1900"),
        "strStadium": fields.String(example="Allianz Arena"),
        "intStadiumCapacity": fields.String(example="75000"),
    },
)


@ns.route("/")
class TeamSearch(Resource):
    @ns.doc(
        params={
            "name": {
                "description": "Team name to search for",
                "type": "string",
                "default": "Bayern Munich",
            }
        }
    )
    @ns.response(200, "Success", [team_model])
    @ns.response(404, "Team not found")
    @ns.response(400, "Missing name parameter")
    def get(self):
        team_name = request.args.get("name")
        if not team_name:
            ns.abort(400, "Please provide a team name using ?name=TeamName")

        teams = fetch_team_data(team_name)
        if not teams:
            ns.abort(404, f"No team found for '{team_name}'")
        return teams
