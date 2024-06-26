from src.model.actions import Actions


class QrCode:
    def __init__(
        self, id: int = None, time: str = None, code: str = None, action: Actions = None
    ):
        self.id = id
        self.time = time
        self.code = code
        self.action = action

    def parse(self, data):
        self.id = data["id"]
        self.time = data["time"]
        self.code = data["code"]
        self.action = Actions().parse(data["action"])
        return self

    def serialize(self):
        return {
            "id": self.id,
            "time": self.time,
            "code": self.code,
            "action": self.action.serialize(),
        }
