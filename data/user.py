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


my_test_user = User(
    first_name="Anna",
    last_name="MyLastName",
    email="kaktus54au@gmail.com",
    gender="Female",
    phone="9138018444",
    year="1983",
    month="April",
    day="09",
    subject="Biology",
    hobbies=["Sports", "Music"],
    picture="kitty.jpeg",
    address="Tomsk Any Street, 123",
    state="Rajasthan",
    city="Jaipur",
)
