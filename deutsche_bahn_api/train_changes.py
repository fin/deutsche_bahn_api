from deutsche_bahn_api.message import Message


class TrainChanges:
    """ This class represents changed train attributes. """
    departure: str
    departure_status: str
    arrival: str
    arrival_status: str
    passed_stations: str
    stations: str
    platform: str
    messages: list[Message]
