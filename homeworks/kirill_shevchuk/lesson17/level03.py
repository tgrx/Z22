def my_map(function, massiv):
    arr = []
    for i in massiv:
        arr.append(function(i))
    return arr
