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
# print(get_data())


def add(a: int, b: int) -> int:
    return a + b

def sub(a, b) -> int:
    return a - b

def mult(a,b) -> int:
    return a*b

def div(a,b) -> float:
    while b==0:
        print("Nie można dzielić przez 0. Proszę wybrać inną liczbę.")
        b = int(input("b = "))
    return a/b



# print(div(a,b))

operations = {
    "1": add,
    "2": sub,
    "3": mult,
    "4": div
}


def main():
    operation, a, b = get_data()
    result = operations[operation](a, b)
    return result

print(main())


# if __name__ == "__main__":
#     main()