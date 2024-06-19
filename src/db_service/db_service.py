from typing import List
from src.model.personel import Personel
from src.model.attandance import Attandance
from src.model.log import Log
from src.model.shift import Shift
from src.db_service.db_service_attandance import AttandanceDbService
from src.db_service.db_service_log import LogService
from src.db_service.db_service_shift import ShiftService
from src.db_service.db_service_personel import PersonelService


class DbService:
    def add_personel(self, personel: Personel):
        personel_service = PersonelService()
        personel_service.add(personel)

    def add_attendance(self, attandance: Attandance):
        attendance_service = AttandanceDbService()
        attendance_service.add(attandance)

    def add_log(self, log: Log):
        log_service = LogService()
        log_service.add(log)

    def add_shift(self, shift: Shift):
        shift_service = ShiftService()
        shift_service.add(shift)

    def delete_personel(self, personel_id: int):
        personel_service = PersonelService()
        personel_service.delete(personel_id)

    def delete_attendance(self, attendance_id: int):
        attendance_service = AttandanceDbService()
        attendance_service.delete(attendance_id)

    def delete_log(self, log_id: int):
        log_service = LogService()
        log_service.delete(log_id)

    def delete_shift(self, shift_id: int):
        shift_service = ShiftService()
        shift_service.delete(shift_id)

    def update_personel(self, personel: Personel):
        personel_service = PersonelService()
        personel_service.update(personel)

    def get_all_personel(self) -> List[Personel]:
        personel_service = PersonelService()
        return personel_service.get_all()

    def get_all_attendance(self) -> List[Attandance]:
        attendance_service = AttandanceDbService()
        return attendance_service.get_all()

    def get_all_log(self) -> List[Log]:
        log_service = LogService()
        return log_service.get_all()

    def get_all_shift(self) -> List[Shift]:
        shift_service = ShiftService()
        return shift_service.get_all()

    def get_personel(self, personel_id: int) -> Personel:
        personel_service = PersonelService()
        return personel_service.get(personel_id)

    def get_attendance(self, attendance_id: int) -> Attandance:
        attendance_service = AttandanceDbService()
        return attendance_service.get(attendance_id)

    def get_log_by_personel_id(self, personel_id: int) -> Log:
        log_service = LogService()
        return log_service.get_by_person_id(personel_id)

    def get_shift(self, shift_id: int) -> Shift:
        shift_service = ShiftService()
        return shift_service.get_by_id(shift_id)
