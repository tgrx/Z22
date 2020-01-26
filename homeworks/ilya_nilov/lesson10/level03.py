def validate_password(paswrd):
    correct_words = 0
    for letters in paswrd:
        if letters.isupper():
            correct_words += 1
        elif correct_words >= 5:
            return 0
    return 5 - correct_words
