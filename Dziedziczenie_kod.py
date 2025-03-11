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

    if rodzaj == "Base":
        for _ in range(ilosc):
            contact = BaseContact(
                name=fake.first_name(),
                surname=fake.last_name(), 
                private_number=fake.phone_number(),
                email_address=fake.email())
            contacts.append(contact)
            
    elif rodzaj == "Business":
        for _ in range(ilosc):
            contact = BusinessContact(
                name=fake.first_name(),
                surname=fake.last_name(), 
                private_number=fake.phone_number(),
                email_address=fake.email(),
                occupation = fake.job(),
                company = fake.company(),
                business_number = fake.phone_number())
            contacts.append(contact)
    return contacts

fake_contacts = create_contacts("Business", 15) # Parametr pierwszy - rodzaj wyzytówki: "Base" lub "Business". Parametr drugi to ilość kontaktów.