from actions import Actions

action = Actions(id=1, name="test")
action0 = Actions().parse(action.serialize())


from qrCode import QrCode

code = QrCode(id=1, time="time", code="code", action=action)
code0 = QrCode().parse(code.serialize())


if __name__ == "__main__":
    print(action0.serialize())
    print(code0.serialize())
