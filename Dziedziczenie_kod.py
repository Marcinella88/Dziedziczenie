# Zadanie: "Dziedziczenie"

from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, name, surname, private_number, email_address):
        self.name = name
        self.surname = surname
        self.private_number = private_number
        self.email_address = email_address
    
    def contact(self):
        print(f"Wybieram numer {self.private_number} i dzwonię do {self.name} {self.surname}")
    
    def __str__(self):
        return f"{self.name}, {self.surname}, {self.private_number}, {self.email_address}"

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)

class BusinessContact(BaseContact):
    def __init__(self, occupation, company, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company = company
        self.business_number = business_number

    def contact(self):
        print(f"Wybieram numer {self.business_number} i dzwonię do {self.name} {self.surname}")

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.private_number}, {self.email_address}, {self.occupation}, {self.company}, {self.business_number}"
 
def create_contacts(rodzaj, ilosc):

    contacts = []

    for _ in range(ilosc):
        if rodzaj == "Base":
            contact = BaseContact(
                name=fake.first_name(),
                surname=fake.last_name(), 
                private_number=fake.phone_number(),
                email_address=fake.email())
            contacts.append(contact)
        elif rodzaj == "Business":
            contact = BusinessContact(
                name=fake.first_name(),
                surname=fake.last_name(), 
                private_number=fake.phone_number(),
                email_address=fake.email(),
                occupation = fake.job(),
                company = fake.company(),
                business_number = fake.phone_number())
            contacts.append(contact)
        else:
            print("Nie wybrano prawidłowego rodzaju. Wybierz Base lub Business!")
            break
    return contacts
    
if __name__ == "__main__":
    rodzaj = str(input("Podaj rodzaj wizytówki: Base - wizytówka podstawowa, Business - wizytówka biznesowa: "))
    ilosc = int(input("Ile wizytówek tego typu chcesz wygenerować? "))
    fake_contacts = create_contacts(rodzaj, ilosc)
    
    for contact in fake_contacts:
        print(contact)