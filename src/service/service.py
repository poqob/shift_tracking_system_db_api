from src.service.service_attandance import AttandanceService
from src.service.service_log import LogService
from src.service.service_personel import PersonelService
from src.service.service_shift import ShiftService
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple  # werkzeug development server
from src.db_service.db_builder import DbBuilder
from src.db_service.db_builder_code_api import DbBuilderCodeAPI
from src.service.service_qrcode import QRCodeService

class Service:
    def __init__(self):
        self.dbBuilder = DbBuilder()
        self.dbBuilderCodeAPI = DbBuilderCodeAPI()
        self.personel_service = PersonelService()
        self.attendance_service = AttandanceService()
        self.log_service = LogService()
        self.shift_service = ShiftService()
        self.qrcode_service = QRCodeService()
        self.dbBuilder.create_database()
        self.dbBuilderCodeAPI.create_database()
        # combining all services
        self.application = DispatcherMiddleware(
            self.personel_service.get_app(),
            {
                "/log": self.log_service.get_app(),
                "/attandance": self.attendance_service.get_app(),
                "/shift": self.shift_service.get_app(),
                "/code": self.qrcode_service.get_app(),
            },
        )


if __name__ == "__main__":
    service = Service()
    run_simple("0.0.0.0", 5000, service.application)
