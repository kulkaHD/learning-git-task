

# class Person:
#     def __init__(self, name, b_year):
#         self.name = name
#         self.b_year = b_year
    
#     @property
#     def age(self):
#         return datetime.now().year - self.b_year

#     @age.setter
#     def age(self, value):
#         self.b_year = datetime.now().year - value

# p = Person("Hannka", 1990)
# print(p.age) # 32
# p.age = 42
# print(p.b_year) # 1980

class Kwadrat:
    def __init__(self, bok):
        self._bok = bok
     
    @property
    def bok(self):
        return self._bok

    @bok.setter
    def bok(self,value):
        if value > 0:
            self._bok = value
        else: raise ValueError (f" bok nie moze byc ujemny")

    @property
    def obwod (self):
        return self._bok*4

    @obwod.setter
    def obwod (self,value):
        if value >=0:
            self._bok = value/4
        else:
            raise ValueError(f"Podana wartość obwodu jest ujemna")

    @property
    def pole (self):
        return self._bok**2
   
    @pole.setter
    def pole (self,value):
        if value >=0:
            self._bok = value**(1/2)
        else:
            raise ValueError(f"Podana wartość pola jest ujemna")

k = Kwadrat(2)
print(k.obwod) #8
print(k.pole)  #4
k.obwod = 24
print (k.bok)  #6
k.pole = 16
print(k.bok)   #4
k.bok
k.obwod=32
print(k.bok)

# def say_louder(func):
#     def wrapper():
#        result = func()
#        return result.upper()
#     return wrapper

# @say_louder
# def say_hello():
#    greeting = "Hello stranger!"
#    return greeting

# say_hello()

# say_hello = say_louder(say_hello)

# print(say_hello())

# class Geeks:
#      def __init__(self):
#           self._age = 0
       
#      # function to get value of _age
#      def get_age(self):
#          print("getter method called")
#          return self._age
       
#      # function to set value of _age
#      def set_age(self, a):
#          print("setter method called")
#          self._age = a
  
#      # function to delete _age attribute
#      def del_age(self):
#          del self._age
     
#      age = property(get_age, set_age, del_age) 
  
# mark = Geeks()
  
# mark.set_age (11)
  
# print(mark.age)

# class Geeks:
#      def __init__(self):
#           self._age = 0
       
#      # using property decorator
#      # a getter function
#      @property
#      def age(self):
#          print("getter method called")
#          return self._age
       
#      # a setter function
#      @age.setter
#      def age(self, a):
#          if(a < 18):
#             raise ValueError("Sorry you age is below eligibility criteria")
#          print("setter method called")
#          self._age = a
  
# mark = Geeks()
  
# mark.age(21)
  
# print(mark.age)