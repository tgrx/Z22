def validate_password(password):
    counter = 0
    for i in password:
        if "A" <= i <= "Z":
            counter += 1
    if counter > 4:
        return 0
    return 5 - counter
