def czy_palindrom(word):
    for i in range (len(word)):
        if word[i]==word[-(i+1)]:
            return True
        else:
            return False

print(czy_palindrom("potop"))