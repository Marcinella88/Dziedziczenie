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

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)
    
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
    
contacts = create_contacts("Business", 15)

for contact in contacts:
    print(contact)




#b_wizytowka_1 = BaseContact(name="Marcelina", surname="Tomaszewska", private_number="111-111-111", email_address="MarcelinaTomaszewska@teleworm.us")
#b_wizytowka_2 = BaseContact(name="Gabrysz", surname="Kwiatkowski", private_number="111-111-222", email_address="GabryszKwiatkowski@rhyta.com")
#b_wizytowka_3 = BaseContact(name="Stefcia", surname="Zielinska", private_number="111-111-333", email_address="StefciaZielinska@dayrep.com")
#b_wizytowka_4 = BaseContact(name="Maryla", surname="Sawicka", private_number="111-111-444", email_address="MarylaSawicka@rhyta.com")

#c_wizytowka_1 = BusinessContact(name="Marcelina", surname="Tomaszewska", private_number="111-111-111", email_address="MarcelinaTomaszewska@teleworm.us", occupation="Slaughterer", company="Security Sporting Goods", business_number="48-111-111-111")
#c_wizytowka_2 = BusinessContact(name="Gabrysz", surname="Kwiatkowski", private_number="111-111-222", email_address="GabryszKwiatkowski@rhyta.com", occupation="Cutting", company="Pioneer Chicken", business_number="48-111-111-222")
#c_wizytowka_3 = BusinessContact(name="Stefcia", surname="Zielinska", private_number="111-111-333", email_address="StefciaZielinska@dayrep.com", occupation="Gaming surveillance officer", company="Lee Wards", business_number="48-111-111-333")
#c_wizytowka_4 = BusinessContact(name="Maryla", surname="Sawicka", private_number="111-111-444", email_address="MarylaSawicka@rhyta.com", occupation="New accounts clerk", company="Integra Design", business_number="48-111-111-444")

#b_wizytowki_all = (b_wizytowka_1,b_wizytowka_2,b_wizytowka_3,b_wizytowka_4)
#c_wizytowki_all = (c_wizytowka_1,c_wizytowka_2,c_wizytowka_3,c_wizytowka_4)

#for dane in b_wizytowki_all:
#    print(dane.name, dane.surname, dane.private_number, dane.email_address)

#for dane in c_wizytowki_all:
#    print(dane.name, dane.surname, dane.occupation, dane.company, dane.business_number)

#for dane in c_wizytowki_all:
#    print(f"{dane.name} {dane.surname} ilość znaków: {dane.label_length}")

#print(c_wizytowka_1.label_length)
