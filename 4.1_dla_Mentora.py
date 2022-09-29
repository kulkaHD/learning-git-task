def czy_palindrom(word):
    """
    Returns True/False if an argument is/is not a palindrome.
    Argument:
    word (string)
    """
    for i in range (len(word)):
        if word[i]==word[-(i+1)]:
            x = True  
        else:
            x = False
            break
    return x
print(czy_palindrom("coroc"))