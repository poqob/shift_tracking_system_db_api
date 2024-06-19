from flask import Flask, request, jsonify
from src.db_service.db_service import DbService
from src.model.shift import Shift


class ShiftService:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        self.dbService = DbService()

    def setup_routes(self):
        @self.app.route("/shiftw")
        def index():
            return "welcomming route for shift."

        # the json data contains the shift.serialize() information.
        @self.app.route("/add_shift", methods=["POST"])
        def add():
            if request.method == "POST":
                shift = Shift().parse(request.json)
                self.dbService.add_shift(shift=shift)

        # the json data contains the shift id. {"id": 1}
        @self.app.route("/delete_shift", methods=["POST"])
        def delete():
            if request.method == "POST":
                self.dbService.delete_shift(shift_id=request.json["id"])

        # returns all the shift in the database as json.
        @self.app.route("/get_all_shift", methods=["GET"])
        def get_all():
            if request.method == "GET":
                shifts = self.dbService.get_all_shift()
                serialized_shifts = [shift.serialize() for shift in shifts]
                return jsonify(serialized_shifts)

        # returns one shift object with the given id.
        @self.app.route("/get_shift_by_id", methods=["GET"])
        def get():
            if request.method == "GET":
                shift = self.dbService.get_shift(request.json["id"])
                return jsonify(shift.serialize())

    def run(self, host="0.0.0.0", port=5000, debug: bool = True):
        self.app.run(host=host, port=port, debug=debug)

    def get_app(self):
        return self.app


if __name__ == "__main__":
    service = ShiftService()
    service.run()
