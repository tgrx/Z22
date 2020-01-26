def validate_password(password):
    five_up_words = 5
    up_letters = 0
    count_changes = 0
    if len(password) == 0:
        count_changes = five_up_words

    else:
        for letter in password:
            if letter.isupper():
                up_letters += 1
                if up_letters > 5:
                    count_changes = 0
                else:
                    count_changes = five_up_words - up_letters
    return count_changes
