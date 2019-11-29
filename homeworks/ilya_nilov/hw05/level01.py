def summa (nmbr1, nmbr2):
    try:
        summ = nmbr1 + nmbr2
    except ValueError:
        return("Неверное значение")
    return(summ)
      