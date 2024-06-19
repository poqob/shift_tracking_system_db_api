from src.model.actions import Actions

action = Actions(id=1, name="test")
action0 = Actions().parse(action.serialize())


from src.model.qrCode import QrCode

code = QrCode(id=1, time="time", code="code", action=action)
code0 = QrCode().parse(code.serialize())

from src.model.shift import Shift

shift = Shift(id=1, entrance_date="entrance_date", exit_date="exit_date")
shift0 = Shift().parse(shift.serialize())

from pkg.file import FOLE


if __name__ == "__main__":
    print(action0.serialize())
    print(code0.serialize())
    print(shift0.serialize())
    vari= FOLE(msg="mesaj")
