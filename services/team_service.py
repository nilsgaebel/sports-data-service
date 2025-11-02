import requests
from dtos.team import Team

API_BASE = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"


def fetch_team_data(team_name: str):
    """Fetch team data from TheSportsDB API"""
    try:
        response = requests.get(API_BASE, params={"t": team_name})
        response.raise_for_status()
        data = response.json()
        teams = data.get("teams")
        if teams:
            return [Team.from_api(team).__dict__ for team in teams]
        return
    except requests.RequestException:
        return None
