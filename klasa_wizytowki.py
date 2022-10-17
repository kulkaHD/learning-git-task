from faker import Faker
fake = Faker("pl_PL")
#  class AddressBook:
#     def __init__(self, name, last_name, company, position, email):
#         self.name = name
#         self.last_name = last_name
#         self.company = company
#         self.position = position
#         self.email = email

# Johnnie = AddressBook(name = "Johnnie", last_name = "Needham", company = "Olympic Sports", position = "Technician", email ="JohnnieMNeedham@rhyta.com" )
# Earl = AddressBook(name = "Earl", last_name = "Sousa", company = "Gantos", position = "Manager", email ="EarlMSousa@armyspy.com" )
# Lisa = AddressBook(name = "Lisa", last_name = "Martin", company = "Carl Durfees", position = "Environmental engineering technician", email ="LisaCMartin@rhyta.com" )
# Eloise = AddressBook(name = "Eloise", last_name = "Mak", company = "FlowerTime", position = "Athletic director", email ="EloiseRMak@dayrep.com" )
# Heidi = AddressBook(name = "Heidi", last_name = "Vasquez", company = "Bugle Boy", position = "Condominium association manager", email ="HeidiIVasquez@jourrapide.com" )

# people = [Johnnie, Earl, Lisa, Eloise, Heidi]

# for man in people:
#     print (man.name, man.last_name, man.company, man.position, man.email)

# print(" ")
# from faker import Faker
# fake = Faker()

# list = []


# class wizytowka:
#     def __init__(self, imie, nazwisko, nazwa_firmy):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.nazwa_firmy = nazwa_firmy

# def createUser():
# list.append(wizytowka(fake.first_name(), fake.last_name(),fake.company()))

# for i in range(3):
#     createUser()
# for i in list:
#     print(i.imie, i.nazwisko, i.nazwa_firmy)

# print(list[0].imie)

# print(" ")
# from faker import Faker
# fake = Faker()
# class wizytownik:
#     def __init__(self, name, job, ssn):
#         self.name = name
#         self.job = job
#         self.ssn = ssn
#     def __str__(self):
#         return f'{self.name} {self.job} {self.ssn}'
#     def __repr__(self):
#         return f'wizytownik(name = {self.name} job = {self.job} ssn = {self.ssn})'


# ludzie = []
# for i in range (3):
#     ludzie.append (wizytownik(fake.name(),fake.job(),fake.ssn()))

# for i in ludzie:
#     print(i.name, i.job, i.ssn)

# print(ludzie[0].name)

# print(ludzie[0])


# class AddressBook:
#     def __init__(self, name, last_name, email):
#         self.name = name
#         self.last_name = last_name
#         self.email = email
#     def __str__(self):
#         return f'{self.name} {self.last_name} {self.email}'
#     def contact (self):
#         print (f" Kontaktuję się z {self}")
#     @property
#     def letter_len (self):
#         return (f'{len(self.name)} {len(self.last_name)}')


# Johnnie = AddressBook(name = "Johnnie", last_name = "Needham", email ="JohnnieMNeedham@rhyta.com" )
# Earl = AddressBook(name = "Earl", last_name = "Sousa", email ="EarlMSousa@armyspy.com" )
# Lisa = AddressBook(name = "Lisa", last_name = "Martin", email ="LisaCMartin@rhyta.com" )

# AddressBook.contact(Johnnie)

# ludziki = [Johnnie, Earl, Lisa]


# print(Johnnie.letter_len)

# by_name = sorted(ludziki, key = lambda ludzik: ludzik.name)
# by_last_name = sorted(ludziki, key = lambda ludzik: ludzik.last_name)
# by_email = sorted(ludziki, key = lambda ludzik: ludzik.email)

# for i in by_name:
#     print(f'{i}')

# print(" ")

# for i in by_last_name:
#     print(f'{i}')

# print(" ")

# for i in by_email:
#     print(f'{i}')


import time


class BaseContact:
    def __init__(self, name, last_name, priv_num, email):
        self.name = name
        self.last_name = last_name
        self.priv_num = priv_num
        self.email = email
        
    def __str__(self):
        return f'{self.name} {self.last_name} {self.priv_num} {self.email}'
    @property
    def contact_phone(self):
        return self.priv_num
    def contact (self):
        print (f"Wybieram numer {self.contact_phone} i dzwonię do {self.name} {self.last_name}")


def create_contacts(x=1000):
    card = []
    for i in range(x):
        card.append(BaseContact(name = fake.first_name(), last_name = fake.last_name(), priv_num = fake.phone_number(), email = fake.ascii_free_email()))    
    return card
cardPriv = create_contacts()


