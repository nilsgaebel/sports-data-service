class Team:
    def __init__(
        self,
        idTeam: str,
        strTeam: str,
        strLeague: str,
        intFormedYear: str,
        strStadium: str,
        intStadiumCapacity: str,
    ):
        self.idTeam = idTeam
        self.strTeam = strTeam
        self.strLeague = strLeague
        self.intFormedYear = intFormedYear
        self.strStadium = strStadium
        self.intStadiumCapacity = intStadiumCapacity

    @classmethod
    def from_api(cls, api_data: dict):
        return cls(
            idTeam=api_data.get("idTeam"),
            strTeam=api_data.get("strTeam"),
            strLeague=api_data.get("strLeague"),
            intFormedYear=api_data.get("intFormedYear"),
            strStadium=api_data.get("strStadium"),
            intStadiumCapacity=api_data.get("intStadiumCapacity"),
        )

    def __repr__(self):
        return (
            f"Team(id={self.idTeam!r}, name={self.strTeam!r}, "
            f"league={self.strLeague!r}, stadium={self.stadistrStadiumum!r})"
        )
