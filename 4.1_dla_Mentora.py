def is_palindrome(text):
    """
    Returns True/False if an argument is/is not a palindrome.
    Argument:
    text (string)
    """

    text= ''.join(filter(str.isalnum, text))
    return text.lower() == text[::-1].lower()
  

print(is_palindrome("KoByła ma,mały! bok"))
