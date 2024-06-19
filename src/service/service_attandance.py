from flask import Flask, request, jsonify
from  src.db_service.db_service import DbService
from src.model.attandance import Attandance


class AttandanceService:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        self.dbService = DbService()

    def setup_routes(self):
        @self.app.route("/attandancew")
        def index():
            return "welcomming route for attandance."

        # the json data contains the attandance.serialize() information.
        @self.app.route("/add_attandance", methods=["POST"])
        def add():
            if request.method == "POST":
                attandance = Attandance().parse(request.json)
                self.dbService.add_attendance(attandance=attandance)

        # the json data contains the attandance id. {"id": 1}
        @self.app.route("/delete_attandance", methods=["POST"])
        def delete():
            if request.method == "POST":
                self.dbService.delete_attendance(attendance_id=request.json["id"])

        # returns all the attandance in the database as json.
        @self.app.route("/get_all_attandance", methods=["GET"])
        def get_all():
            if request.method == "GET":
                attandances = self.dbService.get_all_attendance()
                serialized_attandances = [
                    attandances.serialize() for attandance in attandances
                ]
                return jsonify(serialized_attandances)

        # returns one attandance object with the given id.
        @self.app.route("/get_attandance", methods=["GET"])
        def get():
            if request.method == "GET":
                attandances = self.dbService.get_all_attendance()
                serialized_attandances = [
                    attandances.serialize() for attandance in attandances
                ]
                return jsonify(serialized_attandances)

    def run(self, host="0.0.0.0", port=5000, debug: bool = True):
        self.app.run(host=host, port=port, debug=debug)

    def get_app(self):
        return self.app


if __name__ == "__main__":
    service = AttandanceService()
    service.run()
