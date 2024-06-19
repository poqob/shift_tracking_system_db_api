from flask import Flask, request, jsonify
from src.db_service.db_service import DbService
from src.model.log import Log


class LogService:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        self.dbService = DbService()

    def setup_routes(self):
        @self.app.route("/logw")
        def index():
            return "welcomming route for log."

        # the json data contains the attandance.serialize() information.
        @self.app.route("/add_log", methods=["POST"])
        def add():
            if request.method == "POST":
                log = Log().parse(request.json)
                self.dbService.add_log(log=log)

        # the json data contains the attandance id. {"id": 1}
        @self.app.route("/delete_log", methods=["POST"])
        def delete():
            if request.method == "POST":
                self.dbService.delete_log(log_id=request.json["id"])

        # returns all the attandance in the database as json.
        @self.app.route("/get_all_log", methods=["GET"])
        def get_all():
            if request.method == "GET":
                logs = self.dbService.get_all_log()
                serialized_logs = [log.serialize() for log in logs]
                return jsonify(serialized_logs)

        # returns one attandance object with the given id.
        @self.app.route("/get_log_by_personel_id", methods=["GET"])
        def get_by_personel_id():
            if request.method == "GET":
                logs = self.dbService.get_log_by_personel_id()
                serialized_logs = [logs.serialize() for log in logs]
                return jsonify(serialized_logs)

    def run(self, host="0.0.0.0", port=5000, debug: bool = True):
        self.app.run(host=host, port=port, debug=debug)

    def get_app(self):
        return self.app


if __name__ == "__main__":
    service = LogService()
    service.run()
