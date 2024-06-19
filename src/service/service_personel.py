from flask import Flask, request, jsonify
from src.db_service.db_service import DbService
from src.model.personel import Personel


# run the application on port 5000 and static ip address.
class PersonelService:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()
        self.dbService = DbService()

    def setup_routes(self):
        @self.app.route("/personelw")
        def index():
            return "welcomming route for personel."

        # the json data contains the personel.serialize() information.
        @self.app.route("/add_personel", methods=["POST"])
        def add():
            if request.method == "POST":
                personel = Personel().parse(request.json)
                self.dbService.add_personel(personel=personel)

        # the json data contains the personel id. {"id": 1}
        @self.app.route("/delete_personel", methods=["POST"])
        def delete():
            if request.method == "POST":

                self.dbService.delete_personel(personel_id=request.json["id"])

        # The posted data is the personel object to be updated.
        @self.app.route("/update_personel", methods=["POST"])
        def update():
            if request.method == "POST":
                personel = Personel().parse(request.json)
                self.dbService.update_personel(personel=personel)

        # returns all the persones in the database as json.
        @self.app.route("/get_all_personel", methods=["GET"])
        def get_all():
            if request.method == "GET":
                personels = self.dbService.get_all_personel()
                serialized_personels = [personel.serialize() for personel in personels]
                return jsonify(serialized_personels)

        # returns one the of persones in the db with given id.
        @self.app.route("/get_personel", methods=["GET"])
        def get():
            if request.method == "GET":
                personels = self.dbService.get_personel(personel_id=request.json["id"])
                return jsonify(personels.serialize())

    def run(self, host="0.0.0.0", port=5000, debug: bool = True):
        self.app.run(host=host, port=port, debug=debug)

    def get_app(self):
        return self.app


if __name__ == "__main__":
    service = PersonelService()
    service.run()
