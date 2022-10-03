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
def get_data() -> Tuple[str, list, float]:
    op = input('''Podaj numer operacji:
    1 (dodawanie)
    2 (odejmowanie)
    3 (mnożenie)
    4 (dzielenie) ''')
    while op not in ("1","2","3","4"):
        print ("Poproszę o liczbę z zakresu 1-4.")
        op = input('''Podaj numer operacji:
    1 (dodawanie)
    2 (odejmowanie)
    3 (mnożenie)
    4 (dzielenie) ''')

    op_log_info = {
        "1": "Wybrałeś dodawanie.",
        "2": "Wybrałeś odejmowanie.",
        "3": "Wybrałeś mnożenie.",
        "4": "Wybrałeś dzielenie."
        }
    logging.info(op_log_info[op])
    
    if op in ("2", "4"):
        a = input("Wpisz liczbę: ")
        while check_user_input_float(a) == False:
            logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
            a = input("Wpisz liczbę: ")
        a = float(a)
    else:
        a=[]
        how_many_num = (input("Ile liczb potrzebujesz w swojej operacji? "))
        while check_user_input_int(how_many_num) == False:
            logging.info("Nie wpisałeś liczby całkowitej. Wpisz liczbę całkowitą.")
            how_many_num = input("Ile liczb potrzebujesz w swojej operacji? ")
        how_many_num = int(how_many_num) 
        for i in range (how_many_num-1):
            x = input("Wpisz liczbę: ")
            while check_user_input_float(x) == False:
                logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
                x = input("Wpisz liczbę: ")
            x = float(x)
            a.append (x)
    
    b = input("Wpisz liczbę: ")
    while check_user_input_float(b) == False:
        logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
        b = input("Wpisz liczbę: ")
    b = float(b)
    while op == "4" and b == 0:
        logging.warning("Nie można dzielić przez 0. Proszę wybrać inną liczbę.")
        b = input("Wpisz liczbę: ")
        while check_user_input_float(b) == False:
            logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
            b = input("Wpisz liczbę: ")
        b = float(b)
   
    return op, a, b
    

def add(a: list, b: float) -> float:
    return sum(a,b)

def sub(a: float, b: float) -> float:
    return a - b

def mult(a: list, b: float) -> float:
    for i in a:
        b *=i     
    return b

def div(a: float, b: float) -> float:
    return a / b

operations = {
    "1": add,
    "2": sub,
    "3": mult,
    "4": div
    }

def main() -> float:
    operation, a, b = get_data()
    result = operations[operation](a, b)
    print ("wynik to: ", "%.2f" % result)
    if __name__ == "__main__":
        print ("Jaki fajny kalkulator,ciekawe,czy ktos w innym programie go będzie uzywał?")
    return result

main()
