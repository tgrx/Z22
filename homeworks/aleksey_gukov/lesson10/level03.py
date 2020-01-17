def validate_password(pas):
    big_letter = 0
    for letter in pas:
        if letter.isupper():
            big_letter += 1
    if big_letter >= 5:
        answer = 0
    else:
        answer = 5 - big_letter
    return answer
