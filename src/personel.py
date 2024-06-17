class Personel:
    def __init__(
        self,
        id_number: int = None,
        name: str = None,
        surname: str = None,
        mail: str = None,
        password: str = None,
    ):
        self.id_number = id_number
        self.name = name
        self.surname = surname
        self.mail = mail
        self.password = password

    @staticmethod
    def parse(json_data):
        id_number = json_data.get("id_number")
        name = json_data.get("name")
        surname = json_data.get("surname")
        mail = json_data.get("mail")
        password = json_data.get("password")
        return Personel(id_number, name, surname, mail, password)

    def serialize(self):
        return {
            "id_number": self.id_number,
            "name": self.name,
            "surname": self.surname,
            "mail": self.mail,
            "password": self.password,
        }

    def __str__(self):
        return f"Personel(id_number={self.id_number}, name={self.name}, surname={self.surname}, mail={self.mail}, password={self.password})"
