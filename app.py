from flask import Flask
from flask_restx import Api
from resources.team_resource import ns as team_namespace
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(
    app,
    version="1.0",
    title="Sports API",
    description="This API provides access to sports data using TheSportsDB",
)

# Register namespace
api.add_namespace(team_namespace, path="/teams")

if __name__ == "__main__":
    app.run(debug=True)
