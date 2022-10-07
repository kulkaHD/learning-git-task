class BaseContact:
    def __init__(self, name, last_name, priv_num, email):
        self.name = name
        self.last_name = last_name
        self.priv_num = priv_num
        self.email = email
        self._contact = (f"Wybieram numer {self.priv_num} i dzwonię do {self.name} {self.last_name}")
    def __str__(self):
        return f'{self.name} {self.last_name} {self.priv_num} {self.email}'
    def contact (self):
        print (self._contact)
        #to jest wersja na potrzeby podklasy. W innym wypadku ta metoda wygladalaby tak:
    # def contact (self):
    #     print (f"Wybieram numer {self.priv_num} i dzwonię do {self.name} {self.last_name}")        
    @property
    def label_length(self):
        return len(self.name) + len(self.last_name)
  

class BusinessContact (BaseContact):
    def __init__(self, job, company, work_num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.work_num = work_num
        self._contact = (f"Wybieram numer {self.work_num} i dzwonię do {self.name} {self.last_name}")
    def __str__(self):  
        return f'{self.name} {self.last_name} {self.job} {self.company} {self.work_num}'
        # domyślnie , bez _str_(self), print(bus1) pokaze te same dane, co print (priv1).
        # Zeby danych bylo wiecej o te dodatkowe z zakresu "business"- muszę jeszcze raz def__str__, tak jak powyzej?
    def contact (self):
        super().contact()
        # czy moze tak się obchodzi system i tak się robi super metody zawierające nieco zmienione parametry?

priv1 = BaseContact(name = "Johnnie", last_name = "Needham", priv_num = "587413698", email ="JohnnieMNeedham@rhyta.com")
priv2 = BaseContact(name = "Earl", last_name = "Sousa", priv_num = "439852175", email ="EarlMSousa@armyspy.com")
priv3 = BaseContact(name = "Lisa", last_name = "Martin", priv_num = "985632147", email ="LisaCMartin@rhyta.com")

bus1 = BusinessContact(name = "Johnnie", last_name = "Needham", priv_num = "587413698", email ="JohnnieMNeedham@rhyta.com", job = "manager", company = "IBM", work_num = "999874159")
bus2 = BusinessContact(name = "Earl", last_name = "Sousa", priv_num = "439852175", email ="EarlMSousa@armyspy.com", job = "tiger assistant", company = "ZOO", work_num = "632587412")
bus3 = BusinessContact(name = "Lisa", last_name = "Martin", priv_num = "985632147", email ="LisaCMartin@rhyta.com", job = "scientist", company = "DATA", work_num = "638741874")


BaseContact.contact(priv1)
BusinessContact.contact(bus1)
print(bus1)
print(priv1.label_length)
print(bus2.label_length)