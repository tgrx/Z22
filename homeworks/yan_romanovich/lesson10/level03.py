def validate_password(password):
    result = 0
    for i in password:
        if "A" <= i <= "Z":
            result += 1
    if 5 - result > 0:
        return 5 - result
    return 0
