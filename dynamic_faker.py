import faker

f = faker.Faker()


class Contact:
    def __init__(self):
        self.firstname = f.first_name()
        self.lastname = f.last_name()
        self.email = f""

    def __str__(self) -> str:
        return f"{self.firstname}, {self.lastname}"
