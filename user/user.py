import dataclasses

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    month: str
    year: str
    day: str
    subject: str
    hobbies: [str]
    picture: str
    address: str
    state: str
    city: str
