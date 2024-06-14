class Qrcode:
    def __init__(self, id=None, time=None, code=None, action=None):
        self.id = id
        self.time = time
        self.code = code
        self.action = action

    @staticmethod
    def parse(self, data):
        self.id = data["id"]
        self.time = data["time"]
        self.code = data["code"]
        self.action = data["action"]
        return self
