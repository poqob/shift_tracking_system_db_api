from flask import Flask, request, g, jsonify
from io import BytesIO
import base64
from src.model.actions import Actions
from src.db_service.db_service_qrcode import DbQrcodeService
from src.db_service.db_service_actions import DbActionsService
from src.util.qrcode_generator import generateRandomQr


# run the application on port 5000 and static ip address.
class QRCodeService:
    def __init__(self):
        self.app = Flask(__name__)
        self.last_code = None
        self.setup_routes()
        self.dbService = DbQrcodeService()
        self.dbActionsService = DbActionsService()

    def serve_pil_image(self, pil_img):
        img_io = BytesIO()
        pil_img.save(img_io, format="PNG")  # You can choose other formats like JPEG
        img_io.seek(0)
        encoded_data = base64.b64encode(img_io.getvalue()).decode("utf-8")
        return f'<img src="data:image/png;base64,{encoded_data}" />'

    def setup_routes(self):
        @self.app.route("/")
        def index():
            return "welcomming route"

        @self.app.route("/verify", methods=["POST"])
        def verify():
            if request.method == "POST":
                data = request.get_json()
                key = data.get("key")
                if self.dbService.get_by_code(key) is not None:
                    return key
                else:
                    return key + " is not found"

        @self.app.route("/qr", methods=["GET"])
        def qr():
            if request.method == "GET":
                img, self.last_code = generateRandomQr()
                self.dbService.add(
                    action=Actions(id=1), code=self.last_code.code
                )  # db addition
                return self.serve_pil_image(img)

        @self.app.route("/get_all_codes", methods=["GET"])
        def get_all():
            if request.method == "GET":
                codes = self.dbService.get_all()
                serialized_codes = [code.serialize() for code in codes]
                return jsonify(serialized_codes)

        @self.app.route("/get_all_actions", methods=["GET"])
        def get_all_actions():
            if request.method == "GET":
                actions = self.dbActionsService.get_all()
                serialized_actions = [action.serialize() for action in actions]
                return jsonify(serialized_actions)

    def run(self):
        self.app.run(host="0.0.0.0", port=5000, debug=True)

    def get_app(self):
        return self.app


if __name__ == "__main__":
    service = QRCodeService()
    service.run()
