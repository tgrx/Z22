def my_filter(function, spisok):
    arr = []
    for i in spisok:
        if function(i):
            arr.append(i)
    return arr
