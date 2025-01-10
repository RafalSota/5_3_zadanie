from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, name, surname, private_phone, mail):
        self.name = name
        self.surname = surname
        self.private_phone = private_phone
        self.mail = mail
        #Variables
        self._max_lenght_name_surname = 25
    def __str__(self):
        return f'{self.name} {self.surname}, telefon prywatny: {self.private_phone}'
    def contact(self):
        print(f"\nWybieram numer prywatny {self.private_phone} i dzwonię do {self.name} {self.surname}")
    @property
    def label_lenght(self):
        return len(self.name) + 1 + len(self.surname)
    def check_lenght_name_surname(self):
        if self.label_lenght <= self._max_lenght_name_surname:
            print(f"Możemy poprawnie zaadresować kopertę. Imię i nazwisko '{self.name} {self.surname}' posiada {self.label_lenght} znaków, a max to {self._max_lenght_name_surname}")
        else:
            raise ValueError(f"Długość imienia i nazwiska '{self.name} {self.surname}' wynosi {self.label_lenght} i jest większa od max = {self._max_lenght_name_surname}")

class BusinessContact(BaseContact):
    def __init__(self, workstation, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.workstation = workstation
        self.company = company
        self.work_phone = work_phone
    def __str__(self):
        return f'{self.name} {self.surname}, telefon służbowy: {self.work_phone}'
    def contact(self):
        print(f"\nWybieram numer służbowy {self.work_phone} i dzwonię do {self.name} {self.surname}")
    @property
    def label_lenght(self):
        return len(self.name) + 1 + len(self.surname)
    def check_lenght_name_surname(self):
        if self.label_lenght <= self._max_lenght_name_surname:
            print(f"Możemy poprawnie zaadresować kopertę. Imię i nazwisko '{self.name} {self.surname}' posiada {self.label_lenght} znaków, a max to {self._max_lenght_name_surname}")
        else:
            raise ValueError(f"Długość imienia i nazwiska '{self.name} {self.surname}' wynosi {self.label_lenght} i jest większa od max = {self._max_lenght_name_surname}")

BusinessCards = []
BaseCards = []

def create_contacts(type_cards, amount):
    if type_cards == BaseContact:
        print(f"\nTworzę losową listę kontaktów podstawowych: \n")
        for i in range(0, amount):
            person = BaseContact(name=fake.first_name(), surname=fake.last_name(), private_phone = fake.phone_number(), mail=fake.email())
            BaseCards.append(person)
            print(BaseCards[i])
    if type_cards == BusinessContact:
        print(f"\nTworzę losową listę kontaktów biznesowych: \n")
        for i in range(0, amount):
            person = BusinessContact(name=fake.first_name(), surname=fake.last_name(), private_phone=fake.phone_number(), mail=fake.email(), workstation=fake.job(), company=fake.company(), work_phone=fake.phone_number())
            BusinessCards.append(person)
            print(BusinessCards[i])

create_contacts(BaseContact, 13)
BaseCards[7].contact()
BaseCards[7].check_lenght_name_surname()

create_contacts(BusinessContact, 5)
BusinessCards[2].contact()
BusinessCards[2].check_lenght_name_surname()

