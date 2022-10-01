import logging
logging.basicConfig(level=logging.DEBUG)

from typing import Tuple
def get_data() -> Tuple[str, int, int]:
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
    
    a = int(input("a = "))
    b = int(input("b = "))
  
    return op, a, b


def add(a: int, b: int) -> int:
    logging.info("Wybrałeś dodawanie.")
    return a + b

def sub(a: int, b: int) -> int:
    logging.info("Wybrałeś odejmowanie.")
    return a - b

def mult(a: int,b: int) -> int:
    logging.info("Wybrałeś mnożenie.")
    return a * b

def div(a: int,b: int) -> float:
    logging.info("Wybrałeś dzielenie.")
    while b==0:
        logging.warning("Nie można dzielić przez 0. Proszę wybrać inną liczbę.")
        b = int(input("b = "))
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
    if __name__ == "__main__":
        print ("Jaki fajny kalkulator,ciekawe,czy ktos w innym programie go będzie uzywał?")
    return result

main()