# import sys

# def customized_hello (tytul,first_name,last_name):
#     print("hello %s %s %s!" % (tytul,first_name,last_name))
# if __name__ == "__main__":
#     if len(sys.argv) < 4:
#         exit(1)
#     first_name = sys.argv[1]
#     last_name = sys.argv[2]
#     tytul = sys.argv[3]
#     customized_hello(tytul,first_name, last_name)

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



