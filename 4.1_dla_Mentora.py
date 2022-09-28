def czy_palindrom(word):
    """
    Returns True/False if an argument is/is not a palindrome.
    Argument:
    word (string)
    """
    for i in range (len(word)):
        if word[i]==word[-(i+1)]:
            return True
        else:
            return False

print(czy_palindrom("potop"))