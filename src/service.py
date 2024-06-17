from service_attandance import AttandanceService
from service_log import LogService
from service_personel import PersonelService
from service_shift import ShiftService
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple  # werkzeug development server
from db_builder import DbBuilder


class Service:
    def __init__(self):
        self.dbBuilder = DbBuilder()
        self.personel_service = PersonelService()
        self.attendance_service = AttandanceService()
        self.log_service = LogService()
        self.shift_service = ShiftService()
        self.dbBuilder.create_database()
        # combining all services
        self.application = DispatcherMiddleware(
            self.personel_service.get_app(),
            {
                "/log": self.log_service.get_app(),
                "/attandance": self.attendance_service.get_app(),
                "/shift": self.shift_service.get_app(),
            },
        )


if __name__ == "__main__":
    service = Service()
    run_simple("0.0.0.0", 5000, service.application)
