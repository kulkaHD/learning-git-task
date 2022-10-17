import sys

def customized_hello (first_name,last_name):
    print("hello %s %s!" % (first_name,last_name))
if __name__ == "__main__":
    print(sys.argv)
    customized_hello("John", "Cleese")

# def shopping(items, payment='card', shop='local shop'):
#     result = ""
#     result = result + "Idę na zakupy do %s.\n" % shop
#     result = result + "Kupię następujące rzeczy:\n"
#     for item in items:
#         result = result + " - %s\n" % item
#     result = result + "By zapłacić, używam %s." % payment
#     return result

# if __name__ == "__main__":
#     items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
#     items = items_text.split(',')
#     shopping_result = shopping(items)
#     print(shopping_result)




