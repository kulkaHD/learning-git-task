"""
    Kalkulator wykonuje następujące operacje:
    - pobiera informacje, które działanie chcemy wykonać (dodawanie, odejmowanie,mnożenie,dzielenie)
    - pobiera wartości dla dwóch argumentów a i b zwracając uwagę użytkownika,gdy nie wpisze on wartości liczbowych. Uzytkownik może wpisać je ponownie.
    - dla dodawania i mnożenia mozliwe jest dodanie dowolnej liczby argumentów - tutaj również uzytkownik może popełniać błędy w wprowadzaniu danych. Może się poprawiać.

"""

import logging
logging.basicConfig(level=logging.DEBUG)

def check_user_input_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False 

def check_user_input_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False 

from typing import Tuple
def get_data() -> Tuple[str, float, float]:
    op = input('''Podaj numer operacji:
    1 (dodawanie)
    2 (odejmowanie)
    3 (mnożenie)
    4 (dzielenie) ''')
    while op != "1" and  op != "2" and  op != "3" and  op != "4":
        print ("Poproszę o liczbę z zakresu 1-4.")
        op = input('''Podaj numer operacji:
    1 (dodawanie)
    2 (odejmowanie)
    3 (mnożenie)
    4 (dzielenie) ''')
    if op == "1":
        logging.info("Wybrałeś dodawanie.")
    elif op == "2":
        logging.info("Wybrałeś odejmowanie.")
    elif op == "3":
        logging.info("Wybrałeś mnożenie.")
    elif op == "4":
        logging.info("Wybrałeś dzielenie.")
    else:
        pass

    a = input("a = ")
    while check_user_input_float(a) == False:
        logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
        a = input("a = ")
    a = float(a)
    
    b = input("b = ")
    while check_user_input_float(b) == False:
        logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
        b = input("b = ")
    b = float(b)
  
    return op, a, b


def add(a: float, b: float) -> float:
    more_numbers = (input("Czy chcesz dodać więcej liczb niż wpisane do tej pory? Wpisz, proszę, tak lub nie: "))
    while more_numbers.lower() != "tak" and  more_numbers.lower() != "nie":
            logging.info("Błędna odpowiedź. Poproszę o odpowiedź tak lub nie.")
            more_numbers = (input("Czy chcesz dodać więcej liczb niż wpisane do tej pory? Wpisz, proszę, tak lub nie: "))
    if more_numbers.lower() == "tak":
        how_many_more = (input("Ile argumentów chcesz dodać? "))
        while check_user_input_int(how_many_more) == False:
            logging.info("Nie wpisałeś liczby całkowitej. Wpisz liczbę całkowitą.")
            how_many_more = input("Ile argumentów chcesz dodać? ")
        how_many_more = int(how_many_more) 
        all_numbers = [a,b]
        for i in range (how_many_more):
            x = input("Wpisz liczbę: ")
            while check_user_input_float(x) == False:
                logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
                x = input("Wpisz liczbę: ")
            x = float(x)
            all_numbers.append (x)
        return sum(all_numbers)
    elif more_numbers.lower() == "nie":
        return a + b
    else:
        pass
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mult(a: float, b: float) -> float:
    more_numbers = (input("Czy chcesz przemnożyć więcej liczb niż wpisałeś do tej pory? Wpisz, proszę, tak lub nie: "))
    while more_numbers.lower() != "tak" and  more_numbers.lower() != "nie":
            logging.info("Błędna odpowiedź. Poproszę o odpowiedź tak lub nie.")
            more_numbers = (input("Czy chcesz dodać więcej liczb niż wpisane do tej pory? Wpisz, proszę, tak lub nie: "))
    if more_numbers.lower() == "tak":
        how_many_more = (input("Ile argumentów chcesz dodać? "))
        while check_user_input_int(how_many_more) == False:
            logging.info("Nie wpisałeś liczby całkowitej. Wpisz liczbę całkowitą.")
            how_many_more = input("Ile argumentów chcesz dodać? ")
        how_many_more = int(how_many_more) 
        all_numbers = []
        for i in range (how_many_more):
            x = input("Wpisz liczbę: ")
            while check_user_input_float(x) == False:
                logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
                x = input("Wpisz liczbę: ")
            x = float(x)
            all_numbers.append (x)
        all_numbers = [3,4]
        result = a*b
        for i in range(len(all_numbers)):
            result *= all_numbers[i]
        return result
    elif more_numbers.lower() == "nie":
        return a * b
    else:
        pass      
    return a * b


def div(a: float, b: float) -> float:
    while b==0:
        logging.warning("Nie można dzielić przez 0. Proszę wybrać inną liczbę.")
        b = input("b = ")
        while check_user_input_float(b) == False:
            logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
            b = input("b = ")
        b = float(b)
    return ("%.2f" % (a/b))

operations = {
    "1": add,
    "2": sub,
    "3": mult,
    "4": div
}
def main():
    operation, a, b = get_data()
    result = operations[operation](a, b)
    print ("wynik to: ", result)
    # if __name__ == "__main__":
    #     print ("Jaki fajny kalkulator,ciekawe,czy ktos w innym programie go będzie uzywał?")
    return result

main()
