def rotate_left(digits, step):
    return digits[step:] + digits[:step]
